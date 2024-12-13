# Village Data API

This Flask application provides a RESTful API to interact with a PostgreSQL database containing village data. It allows querying village information and filtering by state.

## Features

- **Retrieve all villages**: Fetch all villages from the database.
- **Filter by state**: Retrieve villages in a specific state.

## Prerequisites

- Python 3.x
- PostgreSQL database
- Required Python libraries:
  - `psycopg2`
  - `Flask`

## Installation

1. Clone the repository or download the code.
2. Install the required Python libraries:
   ```bash
   pip install psycopg2 flask

Set up a config.json file in the root directory with the following format:

{
    "database": {
        "host": "<your-database-host>",
        "database": "<your-database-name>",
        "user": "<your-database-username>",
        "password": "<your-database-password>"
    }
}

Ensure your PostgreSQL database is running and contains a table named tbl_mimu_villages with the following structure:

village
villagetract
township
district
states

Usage
Start the Flask application:

python app.py

Access the API endpoints:

Get all villages
Endpoint: GET /village/
Example:

curl http://<host>:8000/village/
Get villages by state
Endpoint: GET /village/states/<states>
Example:

curl http://<host>:8000/village/states/<state-name>

API Endpoints
1. Get All Villages
Request:
GET /village/

Response:

Success (HTTP 200):
[
    ["Village1", "Tract1", "Township1", "District1", "State1"],
    ["Village2", "Tract2", "Township2", "District2", "State2"]
]

Failure (HTTP 404):
{"message": "No villages found!!!."}


2. Get Villages by State

Request:
GET /village/states/<states>

Response:

Success (HTTP 200):
[
    ["Village1", "Tract1", "Township1", "District1", "State1"],
    ["Village2", "Tract2", "Township2", "District2", "State1"]
]
Failure (HTTP 404):
{"message": "No villages found for State '<states>'."}


Notes
The config.json file must be correctly configured for the database connection to work.
Ensure the database is accessible from the host where the application is running.
Use appropriate firewall and security measures to protect the API and database.