from fastapi import FastAPI , APIRouter
import os

# base_router = APIRouter()

# @base_router.get("/")


# def welcome():
#     return {"message": "Welcome to Mini RAG Application vid 6"}

#------

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")


# def welcome():
#     return {"message": "Welcome to Mini RAG With Prefix & Tag"}

## test Prefix --> http://localhost:5000/api/v1/

async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {"message": f"Welcome to app_name ={app_name} & app_version ={app_version}"}

## test using --> http://localhost:5000/api/v1/