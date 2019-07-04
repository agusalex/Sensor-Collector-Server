import sqlite3

db = sqlite3.connect('data/probemon.db')
c = db.cursor()

c.execute("SELECT * FROM mac")
print(c.fetchall())
print(c.fetchone())
print(c.fetchone())
db.commit()

db.close()
