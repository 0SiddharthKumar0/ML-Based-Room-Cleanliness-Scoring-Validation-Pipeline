from sqlalchemy.orm import Session

from app.db.models import AuditLog


def create_audit_log(
    db: Session,
    action: str,
    inspection_id: int = None,
    performed_by: int = None
):
    log = AuditLog(
        action=action,
        inspection_id=inspection_id,
        performed_by=performed_by
    )

    db.add(log)
    db.commit()

    return log