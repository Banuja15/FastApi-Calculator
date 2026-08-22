from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from fastapi_calculator.service import calculate
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),"static")
class CalculatorResponse(BaseModel):
    result:float|int

class CalculatorRequest(BaseModel):
    expression: str
    

@app.get("/")
def root():
    return FileResponse("static/index.html") 

    
@app.post("/calculate",response_model=CalculatorResponse)
def _calculate_(Req:CalculatorRequest):
    try:
        return {"result":calculate(Req.expression)}
    except ZeroDivisionError:
        raise HTTPException(400,"Cannot Divide By Zero")



