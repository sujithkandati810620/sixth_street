from pydantic import BaseModel

class StockData(BaseModel):
    open: float
    high: float
    low: float
    close: float
    volume: int
