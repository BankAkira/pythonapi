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
    BmiValue = calbmi.weight / ((calbmi.height/100)**2)
    bmicate = {}
    if(BmiValue < 18.5):
        bmi_category = "Underweight"
    elif(BmiValue >= 18.5 and BmiValue <= 24.9):
        bmi_category = "Healthy Weight"
    elif(BmiValue >= 25.0 and BmiValue <= 29.9):
        bmi_category = "Overweight"
    else:
        bmi_category = "Obesity"
    
    bmicate = { 
        "Name": calbmi.Name,
        "height": calbmi.height,
        "weight": calbmi.weight ,
        "bmi": BmiValue,
        "bmi_category": bmi_category
    }

    return bmicate

'''
{
    "Name": "John",
    "height": 1.75,
    "weight": 70,
    "bmi": 22.86,
    "bmi_category": "Healthy Weight"
}
'''