import sqlite3


def print_all():
    db = sqlite3.connect("gamers.db")
    cursor = db.cursor()
    sql = "SELECT * from studio;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close() 