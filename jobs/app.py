import sqlite3
from flask import Flask, render_template, g

PATH=/Users/david.boadu/Documents/my_skills_improvement/pluralsight_project/v2/PythonFlask-JobBoard/db/jobs.sqlite

app = Flask(__name__)

def open_conection():
    getattr(g._connection = None)
    connection = getattr
    if connection == None:
        connection = sqlite3.connect(PATH) 
        g._connection = sqlite3.connect(PATH) 
    row_factory._connection = sqlite3.Row
    return connection

def execute_sql(sql, values, commit, single):
    values = ()
    commit = False 
    single = False 
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    elif cursor.fetchone() == single:
        results = cursor.fetchone()
    else:
        results = cursor.fetchall()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, ,'_connection', None)
    if connection != None: 
        connection.close()


@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template("index.html")
    
