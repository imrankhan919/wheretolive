from fastapi import APIRouter 

router = APIRouter(prefix="/cities" , tags=["Cities"])

@router.get("/")
def list() :
    return {"message" : "All Cities"}

@router.post("/")
def add_city() :
    return {"message" : f"city created"}

@router.get("/{city_id}")
def get_city(city_id : int) :
    return {"message" : f"{city_id} here"}

@router.put("/{city_id}")
def update_city(city_id : int) :
    return {"message" : f"{city_id} updated"}

@router.get("/{city_id}/history")
def get_histroy(city_id : int) :
    return {"message" : f"{city_id} history"}