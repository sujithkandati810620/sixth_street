import requests
from fastapi import HTTPException
import datetime
import json
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"




# Cache setup
cache = {}

async def get_stock_data(symbol: str, date: str):
    if symbol in cache:
        return cache[symbol]
    
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": ALPHA_VANTAGE_API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Time Series (Daily)" not in data:
        raise HTTPException(status_code=400, detail="Invalid symbol or API error.")
    
    cache[symbol] = data["Time Series (Daily)"]
    
    daily_data = cache[symbol]
    

    # Check if the date exists in the returned data
    if date not in daily_data:
        # If the date is valid but no data exists, return zeroed values
        return {
            "open": 0.0,
            "high": 0.0,
            "low": 0.0,
            "close": 0.0,
            "volume": 0
        }

    # If the date exists in the data, return the actual data
    stock_data = daily_data[date]
    return {
        "open": float(stock_data["1. open"]),
        "high": float(stock_data["2. high"]),
        "low": float(stock_data["3. low"]),
        "close": float(stock_data["4. close"]),
        "volume": int(stock_data["5. volume"]),
    }



async def get_min_price(symbol: str, n: int):
    data = await get_stock_data(symbol, "latest")
    daily_data = cache[symbol]
    low_prices = [float(daily_data[date]["3. low"]) for date in list(daily_data)[:n]]
    return min(low_prices)

async def get_max_price(symbol: str, n: int):
    data = await get_stock_data(symbol, "latest")
    daily_data = cache[symbol]
    high_prices = [float(daily_data[date]["2. high"]) for date in list(daily_data)[:n]]
    return max(high_prices)
