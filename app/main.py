from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.rooms.router import router as room_router
from app.inspections.router import router as inspection_router

from app.review.router import router as review_router

app = FastAPI(
    title="Room Cleanliness Validation Pipeline",
    version="1.0.0"
)
app.include_router(auth_router)
app.include_router(room_router)
app.include_router(inspection_router)
app.include_router(review_router)



@app.get("/")
def root():
    return {
        "message": "Room Cleanliness Validation Pipeline API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }