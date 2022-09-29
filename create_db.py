import sqlite3 as sql

# connect to SQLite
con = sql.connect(
    "postgres://skswsshtsdgrss:8e33867b45d5bf6bfab33a35191654f8a1f1a4326f23bae32f079fb81a709fec@ec2-54-91-223-99.compute-1.amazonaws.com:5432/d8sts52g57acmu")

# Create a Connection
cur = con.cursor()

# Show books table if already added
cur.execute("DROP TABLE IF EXISTS users")

# Create books table  in db_web database
sql = '''CREATE TABLE "books" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"BOOKNAME"	TEXT,
	"AUTHOR"	TEXT,
	"COVER" BLOB 
)'''
cur.execute(sql)

# commit changes
con.commit()

# close the connection
con.close()
