# Install Poetry if not installed
install-poetry:
	pip install poetry
# Install dependencies using Poetry
Create lock:
	poetry lock
install:
	poetry install
# Run the FastAPI app using Uvicorn with Poetry
run:
	uvicorn app:app --reload
# Run the tests using Poetry
test:
	pytest tests/test_app.py



