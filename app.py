from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from draww import DrawCode,get_random


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates/")

code = ""
tries = 0

def assign():
    global code
    global tries 
    tries = 0
    code = get_random()
    return DrawCode(code).output()

@app.get("/")
async def root(request:Request):
    return templates.TemplateResponse('index.html', {"request":request, "path":assign()})


@app.get("/new")
async def new():
   return {'msg':'done', 'path':assign()}

    
class CodeData(BaseModel):
    code:str

@app.post("/submit")
async def submit(code_data:CodeData):
    global code
    global tries

    if code_data.code.upper() == code:
        return {'msg':'correct','path':'none'}
    
    tries +=1 
    if tries == 3:
        return {'msg':'toomany','path':assign()}

    return {'msg':'incorrect','path':'none'}


