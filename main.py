from fastapi import FastAPI
from pydantic import BaseModel

class multipy(BaseModel):
    a: int                        # variable: type of variable
    b: int

class BMI(BaseModel):
    height: int
    weight: int
    Name: str   

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

@app.post("/BMI/")
def BMI(calbmi: BMI):
    BmiValue = calbmi.weight / (calbmi.height**2)

    if(BmiValue < 18.5):
        return {"result": calbmi.Name + ", your BMI is less than 18.5 >> Underweight"}
    elif(BmiValue >= 18.5 or BmiValue <= 24.9):
        return {"calbmi.Name, your BMI is 18.5—24.9 >> Healthy Weight"}
    elif(BmiValue >= 25.0 or BmiValue <= 29.9):
        return {"calbmi.Name, your BMI is 25.0—29.9 >> Overweight"}
    else:
        return {"calbmi.Name, your BMI is 30.0 >> Above so Obesity"}

'''
{
    "Name": "John",
    "height": 1.75,
    "weight": 70,
    "bmi": 22.86,
    "bmi_category": "Healthy Weight"
}
'''