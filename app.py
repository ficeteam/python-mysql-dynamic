from flask import Flask, render_template, request, redirect
import pymysql
import os

app = Flask(__name__)

conn = pymysql.connect(
    host="root.mysql.database.azure.com",
    user="userroot",
    password="Rohit@123",
    database="newdatabase",
    port=3306,
    ssl={"ssl": {}}
)

@app.route("/")
def home():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employee")
    data = cursor.fetchall()
    print(data)
    return render_template('index.html',employees=data)

@app.route("/submit", methods=["POST"])
def submit():
    id = request.form["id"]
    firstname = request.form["firstName"]
    lastname = request.form["lastName"]

    cursor = conn.cursor()
    query = "INSERT INTO Employee (id,firstname,lastname) VALUES (%s,%s, %s)"
    cursor.execute(query, (id,firstname, lastname))
    conn.commit()

    return redirect ('/')



if __name__ == "__main__":
    app.run()