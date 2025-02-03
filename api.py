from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schemas.loginschema import LoginSchema
from schemas.checklistschema import CheckListSchema
from controllers.login_controller import LoginController
from controllers.api_controller import CheckListController

app = FastAPI()

login_controller = LoginController()
check_list_controller = CheckListController()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login/{usuario}/{senha}", response_model=dict)
async def login_page(data: LoginSchema):
    return JSONResponse(content= await login_controller.is_valid_login(data), status_code=200)

@app.post("/checklist", response_model=dict)
async def check_list(data: CheckListSchema):
    return JSONResponse(content= await check_list_controller.is_check_list_car(data), status_code=200)
