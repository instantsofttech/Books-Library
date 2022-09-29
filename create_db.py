import sqlite3 as sql

# connect to SQLite
con = sql.connect(
    'postgres://nqqltkvqgqstcz:c9a3e77f7483c7d2221e44279ae1b8092cdc093dc3f4f5aa59e5deb5726f872a@ec2-44-210-36-247.compute-1.amazonaws.com:5432/d9jruue7k2ikb')

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
