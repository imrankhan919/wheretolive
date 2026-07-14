from fastapi import APIRouter

router = APIRouter(prefix="/auth" , tags=["Auth"])


@router.post("/login") 
def login() :
    return {"message" : "User Logged In"}

@router.post("/register") 
def register() :
    return {"message" : "User Registred"}

@router.get("/profile") 
def get_profile() :
    return {"message" : "User Profile Here.."}