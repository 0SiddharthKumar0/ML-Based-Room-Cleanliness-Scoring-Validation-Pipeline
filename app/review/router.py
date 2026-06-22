from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.review.schemas import (
    ReviewRequest
)

from app.review.service import (
    review_inspection
)

router = APIRouter(
    prefix="/review",
    tags=["Supervisor Review"]
)


@router.post("/{inspection_id}")
def review_room(
    inspection_id: int,
    request: ReviewRequest,
    db: Session = Depends(get_db)
):
    return review_inspection(
        db,
        inspection_id,
        request.supervisor_id,
        request.final_decision
    )