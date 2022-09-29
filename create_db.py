import sqlite3 as sql

# connect to SQLite
con = sql.connect(
    'postgres://acgqiwenxquwam:8dbc253e737f6e1c7441bfe71a7c080d8c354f4a9c9171528e4c0cf98f91f214@ec2-3-229-252-6.compute-1.amazonaws.com:5432/d4esd7evbkcdr0')

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
