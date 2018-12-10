from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def root():
	return render_template('home.html'), 200

@app.route("/pages/")
def pages():
	conn = sqlite3.connect("pagesDB.db")
	conn.row_factory = sqlite3.Row
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM posts")
	rows=cursor.fetchall();
	return render_template('pages.html', rows=rows), 200

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
