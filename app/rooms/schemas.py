from pydantic import BaseModel


class RoomCreate(BaseModel):
    room_number: str
    floor: int
    room_type: str
    status: str