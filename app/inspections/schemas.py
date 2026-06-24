from pydantic import BaseModel


class InspectionCreate(BaseModel):
    room_id: int
    staff_id: int