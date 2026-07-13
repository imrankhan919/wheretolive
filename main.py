from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message" : "WELCOME TO WHERE TO LIVE API 1.0"}