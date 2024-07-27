from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!!"}

@app.get("/scores/{score}")
def read_score(score: int):
    return {"score": score}