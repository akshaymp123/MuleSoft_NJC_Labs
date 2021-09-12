import sqlite3
mv = sqlite3.connect(movies.db)
c= mv.cursor()
c.execute("SELECT * FROM movies")
items = c.fetchall()

for item in items:
    print(item) 
mv.commit()
mv.close