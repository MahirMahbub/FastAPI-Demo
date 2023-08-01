from typing import Optional

from fastapi import FastAPI, Depends, Query, Path, APIRouter
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from app.depends.db_depend import get_db

example_router = APIRouter()

@example_router.get("/")
def read_root():
    return {"Hello": "World"}