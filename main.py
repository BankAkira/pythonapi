from fastapi import FastAPI
from pydantic import BaseModel

class multiply(BaseModel):
    a: int
    b: int

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!!"}

@app.get("/scores/{score}")
def read_score(score: int):
    return {"score": score}

@app.post("/multiply/")
def multiply(number: multiply):
    return {"result": number.a * number.b}