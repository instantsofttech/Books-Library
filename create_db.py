import sqlite3 as sql

# connect to SQLite
con = sql.connect(
    'postgres://lrlbchnwvdboux:faf52d41bc1ec2c26c4bc258bed2601d0924d981b2b5e09790d0223f08bd3573@ec2-3-219-19-205.compute-1.amazonaws.com:5432/dbibce2inlbpli')

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
