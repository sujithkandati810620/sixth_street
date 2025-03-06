from fastapi import FastAPI
from controllers import stock_lookup, stock_min_max

# Create the FastAPI app instance
app = FastAPI()

# Include routes for stock lookup and min/max endpoints
app.include_router(stock_lookup.router)
app.include_router(stock_min_max.router)

# Run the app using: uvicorn app:app --reload
