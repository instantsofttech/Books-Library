

from fileinput import filename
from flask import Flask, render_template, request, redirect, url_for, flash, abort
import sqlite3 as sql
import os
from resizeimage import resizeimage
from PIL import Image


app = Flask(__name__)
#app.config['UPLOAD_DIR'] = 'static/Uploads'
#root_dir = r'C:\Users\punit\Desktop\ABCD\crudapp\static\Uploads'


# def get_post(uid):
#    con = sql.connect("db_web.db")
#    con.row_factory = sql.Row
#   book = con.execute('SELECT * FROM books WHERE uid = ?', (uid,)).fetchone()
#   con.close()
#   if book is None:
#       abort(404)
#   return book


@app.route("/")
@app.route("/index")
def index():
    con = sql.connect(
        "db_web.db")
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

        #cover = request.files['cover']
        #cover.save(os.path.join(app.config['UPLOAD_DIR'], cover.filename))
        con = sql.connect(
            "db_web.db")
        cur = con.cursor()
        cur.execute("insert into books(BOOKNAME,AUTHOR) values (?,?)",
                    (bookname, author))
        con.commit()
        flash('Book Added', 'success')

        return redirect(url_for("index"))

    return render_template("add_book.html")


@ app.route("/edit_book/<string:uid>", methods=['POST', 'GET'])
def edit_book(uid):
    if request.method == 'POST':
        bookname = request.form['bookname']
        author = request.form['author']
     #  /* cover = request.files['cover']*/
        con = sql.connect(
            "db_web.db")
        cur = con.cursor()
        cur.execute("update books set BOOKNAME=?,AUTHOR=? where UID=?",
                    (bookname, author, uid))
        con.commit()
        flash('Book Updated', 'success')
        return redirect(url_for("index"))
    con = sql.connect(
        "db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from books where UID=?", (uid,))
    data = cur.fetchone()
    return render_template("edit_book.html", datas=data)


@ app.route("/delete_book/<string:uid>", methods=['GET'])
def delete_book(uid):
    con = sql.connect(
        "db_web.db")
    cur = con.cursor()
    cur.execute("delete from books where UID=?", (uid,))
    con.commit()
    flash('Book Deleted', 'warning')
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)
