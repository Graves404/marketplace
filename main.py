import os
import psycopg2
from flask import Flask, render_template, url_for, request, redirect
from markupsafe import escape


app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='postgres',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

@app.route("/")
def hello_world():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    user = cur.fetchall()
    cur.close()
    conn.close()
    print(user)
    return f"index {user}"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/test")
def index():
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return f"login page"
