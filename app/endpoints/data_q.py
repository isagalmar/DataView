from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def root_data():
    return "Hola"