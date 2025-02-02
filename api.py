from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/pageinicial")
def login_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "Usuário"})
