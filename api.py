from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from schemas.loginschema import LoginSchema
from controllers.login_controller import LoginController

app = FastAPI()

login_controller = LoginController()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/login/{usuario}/{senha}", response_model=dict)
async def login_page(data: LoginSchema):
    return JSONResponse(content= await login_controller.loginvalidate(data), status_code=200)
