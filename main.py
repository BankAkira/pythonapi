from fastapi import FastAPI
from pydantic import BaseModel

class multipy(BaseModel):
    a: int                        # variable: type of variable
    b: int    

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
    
@app.post("/multipy/")
def multipy(number: multipy):
    return {"result": number.a * number.b}