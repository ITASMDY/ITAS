# MySQL Interactive Query Tool

This Python script provides a simple command-line interface for interacting with a MySQL database. It allows users to execute custom SQL queries, view available databases, and list tables in a selected database.

## Features

- Connect to a MySQL database.
- Execute custom SQL queries.
- Display available databases.
- Display tables in the connected database.

## Prerequisites

- Python 3.x
- MySQL database server
- Python library:
  - `mysql-connector-python`

## Installation

1. Clone the repository or download the script.
2. Install the required library:
      pip install mysql-connector-python

Update the getConn() function in the script with your database connection details:
conn = mysql.connector.connect(
    host='<your-database-host>',
    port=3306,
    user='<your-database-username>',
    password='<your-database-password>',
    database='<your-database-name>'
)

Usage
Run the script:
python script.py

Use the menu options to interact with the database:

Option 1: Execute a custom SQL query.
Option 2: List all available databases.
Option 3: List all tables in the current database.
Option 4: Exit the script.

Menu Options
1. Execute SQL Query
Enter any valid MySQL query.
Press Ctrl+C to exit the query input mode and return to the main menu.

2. Show Databases
Displays a list of all databases available on the connected MySQL server.

3. Show Tables
Displays a list of all tables in the currently selected database.

4. Exit
Exit the script.

Example
Main Menu

--- Menu List ---
1. Enter SQL Query
2. Show Databases
3. Show Tables
4. Exit

Query Execution

Enter MySQL Query or press Ctrl+C to exit: > SELECT * FROM students;
(1, 'Alice', 'Physics')
(2, 'Bob', 'Mathematics')

Error Handling
The script handles database connection errors gracefully by displaying the error message.
Invalid SQL queries will raise an exception, which will be printed to the console.

Notes
Ensure the user credentials have appropriate permissions for the database.
Verify that the MySQL server is running and accessible from the script's host.
