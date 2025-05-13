from fastapi import APIRouter

router=APIRouter()

@router.get("/")
def read_rout():
    return{"massage":"welcome to smart biz API"}

@router.get("/hello")
def hello_rout():
    return{"massage":"Hello freind im here to start this project"}
