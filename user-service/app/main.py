from fastapi import FastAPI
from .api.users import users
from .api.db import create_db_and_tables


app = FastAPI(
    openapi_url="/users/openapi.json",
    docs_url="/users/docs"
)

@app.on_event("startup")
def startup():
    create_db_and_tables()


app.include_router(users)