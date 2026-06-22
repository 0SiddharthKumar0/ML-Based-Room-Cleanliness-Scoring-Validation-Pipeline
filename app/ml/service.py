
from sqlalchemy.orm import Session

from app import db
from app.audit.service import create_audit_log
from app.db.models import (
    InspectionImage,
    RoomInspection
)

from app.ml.feature_extractor import (
    extract_features
)

from app.ml.scoring import (
    calculate_scores
)


def score_inspection(
    db: Session,
    inspection_id: int
):
    images = (
        db.query(InspectionImage)
        .filter(
            InspectionImage.inspection_id
            == inspection_id
        )
        .all()
    )

    before_path = None
    after_path = None

    for image in images:

        if image.image_type == "BEFORE_CLEANING":
            before_path = image.image_path

        elif image.image_type == "AFTER_CLEANING":
            after_path = image.image_path

    before_features = extract_features(
        before_path
    )

    after_features = extract_features(
        after_path
    )

    cleanliness_score, confidence_score = (
        calculate_scores(
            before_features,
            after_features
        )
    )

    if confidence_score < 0.80:

        decision = "REVIEW"

    elif cleanliness_score >= 85:

        decision = "PASS"

    elif cleanliness_score >= 60:

        decision = "REVIEW"

    else:
        decision = "REJECT"

    inspection = (
    db.query(RoomInspection)
    .filter(
        RoomInspection.id == inspection_id
    )
    .first()
    )


    inspection.cleanliness_score = float(cleanliness_score)

    inspection.confidence_score = float(confidence_score)

    inspection.ml_decision = decision

    db.commit()
    db.refresh(inspection)

    create_audit_log(
        db,
        "ML_SCORING_COMPLETED",
        inspection_id
    )

    return inspection