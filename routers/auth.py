from fastapi import APIRouter , Depends, HTTPException
from sqlmodel import Session , select
from database import get_session
from models.user import User
from services.auth_service import hash_password

router = APIRouter(prefix="/auth" , tags=["Auth"])


@router.post("/login") 
def login() :
    return {"message" : "User Logged In"}

@router.post("/register") 
def register(name : str , email : str , password : str , session : Session = Depends(get_session)) :
    existing = session.exec(select(User).where(User.email == email)).first()
    if existing : 
        raise HTTPException(status_code=400 , detail="User Already Exists")
    user = User(name = name , email = email , password=hash_password(password))
    session.add(user)
    session.commit()
    return {"message" : "User Registred"}

@router.get("/profile") 
def get_profile() :
    return {"message" : "User Profile Here.."}