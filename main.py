import os
from typing import Optional
from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
def inicio(request: Request, error: Optional[str] = None):
    return templates.TemplateResponse(
       name="inicio.html", 
       request=request,
    )

@app.post("/")
def login(usuario: str = Form(...), contrasena: str = Form(...)):
    if contrasena == "1234":
        return RedirectResponse(
            url=f"/bienvenido/{usuario}",
            status_code=status.HTTP_303_SEE_OTHER
        )
    else:
        return RedirectResponse(
            url="/?error=Credenciales+incorrectas", 
            status_code=status.HTTP_303_SEE_OTHER
        )

@app.get("/bienvenido/{usuario}", response_class=HTMLResponse)
def bienvenido(request: Request, usuario: str):


    return templates.TemplateResponse(
        name="bienvenido.html",
        request=request,
    )