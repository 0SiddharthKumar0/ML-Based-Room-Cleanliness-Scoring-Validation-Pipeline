from datetime import datetime

from sqlalchemy.orm import Session
from app.audit.service import create_audit_log


from app.db.models import (
    RoomInspection
)


def review_inspection(
    db: Session,
    inspection_id: int,
    supervisor_id: int,
    final_decision: str
):
    inspection = (
        db.query(RoomInspection)
        .filter(
            RoomInspection.id == inspection_id
        )
        .first()
    )

    inspection.supervisor_id = supervisor_id
    inspection.final_decision = final_decision
    inspection.review_time = datetime.utcnow()

    create_audit_log(
        db,
        "SUPERVISOR_REVIEW_COMPLETED",
        inspection_id,
        supervisor_id
    )

    db.commit()
    db.refresh(inspection)

    return inspection