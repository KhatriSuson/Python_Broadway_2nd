import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database Successfully")


conn.execute(
    """
CREATE TABLE IF NOT EXISTS team_data(
             team text,
             country text,
             season integer,
             total_goals integer);"""
)

conn.commit()
print("Table created successfully")


# try:
conn = sqlite3.connect("test.db")
conn.execute("INSERT INTO team_data VALUES('Real Madrid', 'Spain', 2019, 53);")
conn.execute("INSERT INTO team_data VALUES('PSG', 'Spain', 2019, 53);")
conn.execute("INSERT INTO team_data VALUES(' Barca', 'Spain', 2019, 53);")
conn.execute("INSERT INTO team_data VALUES('Real Madrid', 'Brazil', 2020, 43); ")
conn.execute("INSERT INTO team_data VALUES('PSG', 'Brazil', 2011, 34);")

conn.commit()
# except Exception as e:
#     print(e)


# Average goals by team

conn = sqlite3.connect("test.db")
cursor = conn.execute(
    """SELECT TEAM,
                      AVG(total_goals) AS avg_goals
                      FROM team_data
                      GROUP BY team;"""
)

for row in cursor:
    print(row)


# conn = sqlite3.connect("test.db")
# team_name = input("Enter the team name")
# team = conn.execute(''' SELECT team_name FROM(

# )''')


# Now, the correct query, useing the appropriate sub-query

conn = sqlite3.connect("test.db")
cursor = conn.execute(
    """ SELECT team_name, avg_goals
                      FROM (
                      SELECT team AS team_name,
                      AVG(total_goals) AS avg_goals
                      FROM team_data
                      GROUP BY team
                      ) tp
                      WHERE avg_goals > 50;"""
)

for row in cursor:
    print("Average score",row)