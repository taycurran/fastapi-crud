from fastapi import FastAPI 
import requests

app = FastAPI()

@app.get("/ping")
def pong():
    return {"ping": "pong!"}

