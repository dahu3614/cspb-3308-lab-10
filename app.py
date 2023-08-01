from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://dahu3614:5Z0ZRrCIgEkRyXVoCBapH96xyvfNoLJl@dpg-cj4nf7qcn0vc73eogr2g-a.oregon-postgres.render.com/dahu3614_cspb3308_lab10_db")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://dahu3614:5Z0ZRrCIgEkRyXVoCBapH96xyvfNoLJl@dpg-cj4nf7qcn0vc73eogr2g-a.oregon-postgres.render.com/dahu3614_cspb3308_lab10_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
