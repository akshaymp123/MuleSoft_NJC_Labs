import sqlite3
mv = sqlite3.connect(movies.db)
c= mv.cursor()
c.execute( """CREATE TABLE movies(
                       movie_name text,
                       lead_actor text,
                       actress text,
                       release_year int(10),
                       director text)""")
mv.commit()
mv.close