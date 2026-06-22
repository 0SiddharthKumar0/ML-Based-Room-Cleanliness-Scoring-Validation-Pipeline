from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.rooms.schemas import RoomCreate
from app.rooms.service import (
    create_room,
    get_all_rooms
)

router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)


@router.post("/")
def add_room(
    room: RoomCreate,
    db: Session = Depends(get_db)
):
    created_room = create_room(
        db=db,
        room_number=room.room_number,
        floor=room.floor,
        room_type=room.room_type,
        status=room.status
    )

    return created_room


@router.get("/")
def list_rooms(
    db: Session = Depends(get_db)
):
    return get_all_rooms(db)