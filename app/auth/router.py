from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.auth.schemas import UserRegister
from app.auth.service import create_user


from app.auth.schemas import UserLogin
from app.auth.jwt_handler import create_access_token
from app.auth.service import authenticate_user

from app.db.dependencies import get_db


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/test")
def test_auth():
    return {
        "message": "Authentication router working"
    }


@router.post("/register")
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    try:
        created_user = create_user(
            db=db,
            name=user.name,
            email=user.email,
            password=user.password,
            role=user.role
        )

        return {
            "id": created_user.id,
            "name": created_user.name,
            "email": created_user.email,
            "role": created_user.role
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    authenticated_user = authenticate_user(
        db=db,
        email=user.email,
        password=user.password
    )

    if not authenticated_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        {
            "sub": authenticated_user.email,
            "role": authenticated_user.role,
            "user_id": authenticated_user.id
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }