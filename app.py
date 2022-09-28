
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from books")
    data = cur.fetchall()
    return render_template("index.html", datas=data)


@app.route("/add_book", methods=['POST', 'GET'])
def add_book():
    if request.method == 'POST':
        bookname = request.form['bookname']
        author = request.form['author']
        cover = request.form['cover']
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute("insert into users(UNAME,CONTACT,COVER) values (?,?,?)",
                    (bookname, author, cover))
        con.commit()
        flash('Book Added', 'success')
        return redirect(url_for("index"))
    return render_template("add_book.html")


@app.route("/edit_book/<string:uid>", methods=['POST', 'GET'])
def edit_book(uid):
    if request.method == 'POST':
        bookname = request.form['bookname']
        author = request.form['author']
        cover = request.form['cover']
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute("update books set UNAME=?,CONTACT=?,COVER=? where UID=?",
                    (bookname, author, cover, uid))
        con.commit()
        flash('Book Updated', 'success')
        return redirect(url_for("index"))
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from books where UID=?", (uid,))
    data = cur.fetchone()
    return render_template("edit_book.html", datas=data)


@app.route("/delete_book/<string:uid>", methods=['GET'])
def delete_book(uid):
    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute("delete from books where UID=?", (uid,))
    con.commit()
    flash('Book Deleted', 'warning')
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)
