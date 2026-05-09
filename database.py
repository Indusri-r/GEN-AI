import sqlite3

def create_db():
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    # Drop tables if they exist to recreate with new schema
    cursor.execute("DROP TABLE IF EXISTS Employees")
    cursor.execute("DROP TABLE IF EXISTS Departments")

    # Create Departments table
    cursor.execute("""
    CREATE TABLE Departments (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    # Create Employees table with department reference
    cursor.execute("""
    CREATE TABLE Employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        salary INTEGER,
        dept_id INTEGER,
        position TEXT,
        hire_date TEXT,
        age INTEGER,
        FOREIGN KEY (dept_id) REFERENCES Departments(id)
    )
    """)

    # Insert departments
    cursor.execute("INSERT INTO Departments VALUES (1, 'IT')")
    cursor.execute("INSERT INTO Departments VALUES (2, 'HR')")
    cursor.execute("INSERT INTO Departments VALUES (3, 'Finance')")
    cursor.execute("INSERT INTO Departments VALUES (4, 'Marketing')")

    # Insert employees
    cursor.execute("INSERT INTO Employees VALUES (1, 'John', 60000, 1, 'Developer', '2020-01-15', 30)")
    cursor.execute("INSERT INTO Employees VALUES (2, 'Alice', 70000, 1, 'Senior Developer', '2019-03-22', 32)")
    cursor.execute("INSERT INTO Employees VALUES (3, 'Bob', 40000, 2, 'HR Specialist', '2021-07-10', 28)")
    cursor.execute("INSERT INTO Employees VALUES (4, 'Charlie', 55000, 3, 'Accountant', '2020-11-05', 29)")
    cursor.execute("INSERT INTO Employees VALUES (5, 'Diana', 65000, 1, 'DevOps Engineer', '2018-09-18', 35)")
    cursor.execute("INSERT INTO Employees VALUES (6, 'Eve', 50000, 4, 'Marketing Manager', '2022-02-14', 27)")
    cursor.execute("INSERT INTO Employees VALUES (7, 'Frank', 75000, 3, 'Finance Director', '2017-12-01', 38)")
    cursor.execute("INSERT INTO Employees VALUES (8, 'Grace', 45000, 2, 'Recruiter', '2021-05-20', 26)")

    conn.commit()
    conn.close()


def run_query(query):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return result