from fastapi import APIRouter, HTTPException
from services.stock_service import get_stock_data
from models.stock_models import StockData
import datetime

router = APIRouter()
#curl -X GET "http://127.0.0.1:8000/lookup?symbol=IBM&date=2025-03-03" -H "accept: application/json"

@router.get("/lookup", response_model=StockData)
async def lookup(symbol: str, date: str):
    # Check if date format is correct
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")  
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid Date")
    try:
        print(f"Fetching data for {symbol} on {date}")
        data = await get_stock_data(symbol, date)
        print(f"Received data: {data}")  
        return StockData(**data)
    # Debug print for error
    except HTTPException as e:
        print(f"Error: {e.detail}")  
        raise e