from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from fastapi_calculator.service import calculate
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path


app=FastAPI()
BASE_DIR = Path(__file__).resolve().parent
app.mount("/static",StaticFiles(directory=BASE_DIR/"static"),"static")
class CalculatorResponse(BaseModel):
    result:float|int

class CalculatorRequest(BaseModel):
    expression: str
    

@app.get("/")
def root():
    return FileResponse(BASE_DIR / "static" / "index.html") 

    
@app.post("/calculate",response_model=CalculatorResponse)
def _calculate_(Req:CalculatorRequest):
    try:
        return {"result":calculate(Req.expression)}
    except ZeroDivisionError:
        raise HTTPException(400,"Cannot Divide By Zero")



