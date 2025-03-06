import pytest
from fastapi.testclient import TestClient
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app  

client = TestClient(app)

# Test for the /lookup endpoint with a valid symbol and date
def test_lookup_valid():
    response = client.get("/lookup?symbol=IBM&date=2017-11-15")
    print(response)
    assert response.status_code == 200
    data = response.json()
    assert "open" in data
    assert "high" in data
    assert "low" in data
    assert "close" in data
    assert "volume" in data

# Test for the /lookup endpoint with an invalid symbol
def test_lookup_invalid_symbol():
    response = client.get("/lookup?symbol=INVALID&date=2025-03-02")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid symbol or API error."}

# Test for the /lookup endpoint with a valid symbol but invalid date
def test_lookup_invalid_date():
    response = client.get("/lookup?symbol=IBM&date=2025-02-30")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid Date"}

# Test for the /min endpoint with a valid symbol and range
def test_min_valid():
    response = client.get("/min?symbol=IBM&n=5")
    assert response.status_code == 200
    data = response.json()
    assert "min" in data

# Test for the /min endpoint with an invalid symbol
def test_min_invalid_symbol():
    response = client.get("/min?symbol=INVALID&n=5")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid symbol or API error."}

# Test for the /max endpoint with a valid symbol and range
def test_max_valid():
    response = client.get("/max?symbol=IBM&n=5")
    assert response.status_code == 200
    data = response.json()
    assert "max" in data

# Test for the /max endpoint with an invalid symbol
def test_max_invalid_symbol():
    response = client.get("/max?symbol=INVALID&n=5")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid symbol or API error."}
