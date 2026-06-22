from sqlalchemy.orm import Session

from app.db.models import RoomInspection
from app.audit.service import create_audit_log



def create_inspection(
    db: Session,
    room_id: int,
    staff_id: int
):
    inspection = RoomInspection(
        room_id=room_id,
        staff_id=staff_id,
        ml_decision="PENDING",
        final_decision="PENDING"
    )

    db.add(inspection)
    db.commit()
    db.refresh(inspection)

    create_audit_log(
        db=db,
        action="CREATE_INSPECTION",
        inspection_id=inspection.id,
        performed_by=staff_id
    )

    return inspection

from app.db.models import InspectionImage


def save_inspection_image(
    db: Session,
    inspection_id: int,
    image_path: str,
    image_type: str
):
    image = InspectionImage(
        inspection_id=inspection_id,
        image_path=image_path,
        image_type=image_type
    )

    db.add(image)
    db.commit()
    db.refresh(image)

    return image