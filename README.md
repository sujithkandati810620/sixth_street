# Stock Price API

This project implements a FastAPI-based web service that allows you to query stock prices. It provides three main endpoints:

1. **/lookup**: Retrieve stock data (open, high, low, close, and volume) for a given symbol and date.
2. **/min**: Get the lowest price (low) of a given stock symbol over the last 'n' days.
3. **/max**: Get the highest price (high) of a given stock symbol over the last 'n' days.

## Requirements

- Python 3.12 or higher: [Download Python 3.12](https://docs.python.org/3.12/)
- Poetry (for dependency management): [Install Poetry](https://python-poetry.org/)
- Make (for running commands): [Install Make](https://www.gnu.org/software/make/)
- AlphaVantage API Key: [Get API Key](https://www.alphavantage.co/support/#api-key)

## Setup Instructions

```bash
git clone https://github.com/sujithkandati810620/sixth_street.git
cd sixth_street/boilerplate

make install   # or: poetry install
make run       # or: poetry run uvicorn app:app --reload
make test      # or: poetry run pytest tests/test_app.py
```


## Curl commands 

```bash
curl -X GET "http://127.0.0.1:8000/lookup?symbol=IBM&date=2023-03-02" -H "accept: application/json"
curl -X GET "http://127.0.0.1:8000/min?symbol=IBM&n=5" -H "accept: application/json"
curl -X GET "http://127.0.0.1:8000/max?symbol=IBM&n=5" -H "accept: application/json"
```
