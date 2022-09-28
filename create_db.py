import sqlite3 as sql

# connect to SQLite
con = sql.connect('db_web.db')

# Create a Connection
cur = con.cursor()

# Show books table if already added
cur.execute("DROP TABLE IF EXISTS users")

# Create books table  in db_web database
sql = '''CREATE TABLE "users" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"UNAME"	TEXT,
	"CONTACT"	TEXT,
	"COVER" BLOB NON NULL
)'''
cur.execute(sql)

# commit changes
con.commit()

# close the connection
con.close()
