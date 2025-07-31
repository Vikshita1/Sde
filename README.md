# Sde
## Milestone 1: Database Design and Loading Data

Completed Tasks:
- Created SQLite database and `product` table
- Loaded `products.csv` using a Python script
- Verified successful data insertion with a SELECT query

How to Run:
1. `python create_table.py`
2. `python load_data.py`
3. `python view_data.py`

 Milestone 2 Completed: Backend API Setup 

- Created a new folder titled "Monthly Bill API" to structure the backend codebase.
- Developed `app.py` using FastAPI to handle HTTP requests and routing.
- Implemented `init_db.py` to initialize the SQLite database using schema defined in `schema.sql`.
- Created and tested a working SQLite schema with tables for managing billing data.
- Verified the API is running successfully using `uvicorn` and accessible at `http://127.0.0.1:8000/`.
 Milestone 3 Completed: Backend Functional API Development ⚙

- Implemented essential API endpoints (`GET`, `POST`, etc.) in `app.py` to interact with billing data.
- Integrated the SQLite database with API routes for fetching and storing records securely.
- Performed testing using Postman and browser to validate each endpoint.
- Ensured robust error handling, proper route naming, and clean code documentation for easier integration.
- Confirmed all files (`app.py`, `init_db.py`, `schema.sql`) work in sync under the `Monthly Bill API` directory.
- Maintained a scalable API architecture to allow future enhancements or frontend linkage.

