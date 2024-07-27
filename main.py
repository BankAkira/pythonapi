from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_root():
    return {"message": "Hello World"}

@app.get("/score/{score}")

def read_score(score: int):
    if (score > 70):
        return {"score pass": score}
    else:
        return {"score fail": score}