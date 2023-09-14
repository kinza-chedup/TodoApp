from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
import models
from database import engine
from routers import auth, todos, admin, users
# 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
app = FastAPI()
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)



