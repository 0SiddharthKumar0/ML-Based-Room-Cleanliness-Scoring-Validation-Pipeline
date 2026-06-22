from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy import DateTime, Numeric
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)

    role = Column(String(20), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)

    room_number = Column(String(20), unique=True, nullable=False)
    floor = Column(Integer)
    room_type = Column(String(50))
    status = Column(String(30))

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class RoomInspection(Base):
    __tablename__ = "room_inspections"

    id = Column(Integer, primary_key=True, index=True)

    room_id = Column(Integer, ForeignKey("rooms.id"))
    staff_id = Column(Integer, ForeignKey("users.id"))

    cleanliness_score = Column(Numeric(5, 2))
    confidence_score = Column(Numeric(5, 2))

    ml_decision = Column(String(20))
    final_decision = Column(String(20))

    supervisor_id = Column(Integer, ForeignKey("users.id"))

    inspection_time = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    review_time = Column(DateTime(timezone=True))

    room = relationship("Room")
    staff = relationship(
        "User",
        foreign_keys=[staff_id]
    )
    supervisor = relationship(
        "User",
        foreign_keys=[supervisor_id]
    )


class InspectionImage(Base):
    __tablename__ = "inspection_images"

    id = Column(Integer, primary_key=True, index=True)

    inspection_id = Column(
        Integer,
        ForeignKey("room_inspections.id")
    )

    image_path = Column(Text, nullable=False)
    image_type = Column(String(30), nullable=False)

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    inspection = relationship("RoomInspection")


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    inspection_id = Column(
        Integer,
        ForeignKey("room_inspections.id")
    )

    action = Column(String(100))

    performed_by = Column(
        Integer,
        ForeignKey("users.id")
    )

    old_value = Column(Text)
    new_value = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    inspection = relationship("RoomInspection")
    user = relationship("User")