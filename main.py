from flask import Flask, render_template, redirect, request
from Manager import Manager
from dbInit import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
counter=0

@app.route('/', methods=['GET'])
def home( ):
    result=0
    statement=m.getStatement()
    if statement:
        statement1=statement.statement
    statement=m.getStatement()
    if statement:
        statement2=statement.statement


    return render_template('index.html',statement1=statement1 ,statement2=statement2,result=result)

@app.route('/option1', methods=['POST','GET'])
def option1(result=0):
    global counter
    counter += 1
    statement=m.getStatement()
    if statement:
        statement1=statement.statement
    else:
        statement1=""
    statement=m.getStatement()
    if statement:
        statement2=statement.statement
    else:
        statement2=""

    req=request.form.get("option1")
    m.setScore(req)

    return render_template("index.html" ,statement1=statement1 ,statement2=statement2,result=counter)

@app.route('/option2', methods=['POST','GET'])
def option2():
    global counter
    counter += 1
    statement=m.getStatement()
    if statement:
        statement1=statement.statement
        statement=m.getStatement()
    if statement:
         statement2=statement.statement

    req=request.form.get("option2")
    m.setScore(req)
    return render_template('index.html' ,statement1=statement1 ,statement2=statement2, result=counter)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        m = Manager()
        #m.reset_database()
        m.loadData()

    app.run()
