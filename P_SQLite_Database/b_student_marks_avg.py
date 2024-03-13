import sqlite3

conn = sqlite3.connect("student.db")
print("Opened Student database successfully")


conn.execute(
    """
CREATE TABLE IF NOT EXISTS Student(
             id  INTEGER PRIMARY KEY, 
             name TEXT  NOT NULL,
             subject TEXT,
             marks int
);
"""
)

conn.commit()
print("Table created!")

# Insert data in table

# conn = sqlite3.connect("student.db")
# conn.execute("INSERT INTO Student VALUES(001, 'Ram', 'Maths',85);")
# conn.execute("INSERT INTO Student VALUES(002, 'Ram', 'Science',85);")
# conn.execute("INSERT INTO Student VALUES(003, 'Ram', 'English',85);")
# conn.execute("INSERT INTO Student VALUES(004, 'Ram', 'Nepali',85);")
# conn.execute("INSERT INTO Student VALUES(005, 'Ram', 'Social',85);")
# conn.execute("INSERT INTO Student VALUES(006, 'Ram', 'Computer',85);")

# conn.commit()

# Find percentage

conn = sqlite3.connect("student.db")

per = conn.execute(
    """ 
                   SELECT 
                   SUM(marks) as sum_mark
                   FROM Student
                   GROUP BY name


"""
)

for  i in per:
    print("Sum ", i)
    i = int(i[0])

    print("Percentage = ", (i/600) * 100)



# Fetching Data from Table
    fetchData = conn.execute("SELECT * FROM Student WHERE name=?", ("Ram",))
    
    for j in fetchData:
        print(j)