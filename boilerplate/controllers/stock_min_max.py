from fastapi import APIRouter, HTTPException
from services.stock_service import get_min_price, get_max_price

router = APIRouter()
# curl -X GET "http://127.0.0.1:8000/min?symbol=IBM&n=5" -H "accept: application/json"


@router.get("/min")
async def get_min(symbol: str, n: int):
    try:
        return {"min": await get_min_price(symbol, n)}
    except HTTPException as e:
        raise e
    
# curl -X GET "http://127.0.0.1:8000/max?symbol=IBM&n=5" -H "accept: application/json"


@router.get("/max")
async def get_max(symbol: str, n: int):
    try:
        return {"max": await get_max_price(symbol, n)}
    except HTTPException as e:
        raise e
