from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from fastapi import UploadFile
from fastapi import File

from app.inspections.upload_service import save_image
from app.inspections.service import save_inspection_image


from app.inspections.schemas import InspectionCreate
from app.inspections.service import create_inspection

from app.ml.service import score_inspection
from app.audit.service import create_audit_log


router = APIRouter(
    prefix="/inspections",
    tags=["Inspections"]
)


@router.post("/")
def create_new_inspection(
    inspection: InspectionCreate,
    db: Session = Depends(get_db)
):
    created = create_inspection(
        db=db,
        room_id=inspection.room_id,
        staff_id=inspection.staff_id
    )

    return created

@router.post("/{inspection_id}/upload-before")
def upload_before_image(
    inspection_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = save_image(
        inspection_id,
        "before",
        file
    )

    image = save_inspection_image(
        db,
        inspection_id,
        file_path,
        "BEFORE_CLEANING"
    )
    create_audit_log(
    db,
    "BEFORE_IMAGE_UPLOADED",
    inspection_id
    )

    return image

@router.post("/{inspection_id}/upload-after")
def upload_after_image(
    inspection_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = save_image(
        inspection_id,
        "after",
        file
    )

    image = save_inspection_image(
        db,
        inspection_id,
        file_path,
        "AFTER_CLEANING"
    )
    create_audit_log(
    db,
    "AFTER_IMAGE_UPLOADED",
    inspection_id
    )

    return image


@router.post("/{inspection_id}/score")
def score_room_inspection(
    inspection_id: int,
    db: Session = Depends(get_db)
):
    return score_inspection(
        db,
        inspection_id
    )
