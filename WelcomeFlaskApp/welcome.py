from flask import Flask,jsonify,abort,render_template
from datetime import  datetime
from model import db

app = Flask(__name__)

@app.route("/login")
def login():
    return  render_template("login.html")

@app.route("/api/v1/employees")
def get_employees():
    return  jsonify(db)

@app.route("/api/v1/employees/<int:employeeId>")
def get_emp(employeeId):
    try:
        return  db[employeeId]
    except IndexError:
        abort(404)


@app.route("/")
def hello():
    now = datetime.now().strftime("day : %d/%m/%Y time: %H:%M:%S")
    return  f'''
             <h1>
               Welcome to  Flask web application \n{now}
             </h1> 
           '''
