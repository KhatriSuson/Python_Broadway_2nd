import sqlite3

conn = sqlite3.connect("student_manage.db")
print("Opend student manage database successfully")

conn.execute(
    """
CREATE TABLE IF NOT EXISTS student_management (
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             age INTEGER,
             grade INTEGER,
             address TEXT
);
"""
)

conn.commit()
print("Table created")


# # Insert some sample data
# conn = sqlite3.connect("student_management.db")
# conn.execute(
#     "INSERT INTO student_management (name, age, grade, address) VALUES ('Ram', 23, 12, 'ktm');"
# )
