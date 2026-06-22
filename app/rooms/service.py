from sqlalchemy.orm import Session

from app.db.models import Room


def create_room(
    db: Session,
    room_number: str,
    floor: int,
    room_type: str,
    status: str
):
    room = Room(
        room_number=room_number,
        floor=floor,
        room_type=room_type,
        status=status
    )

    db.add(room)
    db.commit()
    db.refresh(room)

    return room


def get_all_rooms(db: Session):
    return db.query(Room).all()