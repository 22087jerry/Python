import sqlite3

db = sqlite3.connect("gamers.db")
cursor = db.cursor()
sql = "SELECT * from studio;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()