import sqlite3

# Create Database and Table
con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    python INTEGER,
    java INTEGER,
    dbms INTEGER,
    total INTEGER,
    percentage REAL,
    result TEXT
)
""")

con.commit()

# Menu
while True:
    print("\n====== STUDENT MARK SHEET SYSTEM ======")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Read/View Student")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. View Result")
    print("7. Reports")
    print("8. Exit")

    ch = int(input("Enter Choice: "))

    # Add Student
    if ch == 1:
        id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")

        python = int(input("Enter Python Marks: "))
        java = int(input("Enter Java Marks: "))
        dbms = int(input("Enter DBMS Marks: "))

        total = python + java + dbms
        percentage = total / 3

        if python >= 35 and java >= 35 and dbms >= 35:
            result = "Pass"
        else:
            result = "Fail"

        cur.execute(
            "INSERT INTO student VALUES (?,?,?,?,?,?,?,?)",
            (id, name, python, java, dbms, total, percentage, result)
        )

        con.commit()
        print("Student Record Added Successfully!")

    # Update Student
    elif ch == 2:
        print("Update Option")

    # Read/View Student
    elif ch == 3:
        print("View Option")

    # Search Student
    elif ch == 4:
        print("Search Option")

    # Delete Student
    elif ch == 5:
        print("Delete Option")

    # View Result
    elif ch == 6:
        print("Result Option")

    # Reports
    elif ch == 7:
        print("Reports Option")

    # Exit
    elif ch == 8:
        con.close()
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
