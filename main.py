from flask import Flask, render_template, redirect, request
from Manager import Manager
from dbInit import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
counter=0

@app.route('/', methods=['GET'])
def home():
    result=0
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

    return render_template('index.html',statement1=statement1 ,statement2=statement2,result=result)

@app.route('/option1', methods=['POST','GET'])
def option1():
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
    notEnd,allFive=m.setScore(req)
    if notEnd:
        return render_template("index.html" ,statement1=statement1 ,statement2=statement2,result=counter)
    else:
        return render_template("results.html",neuroticism=allFive.neuroticism,opennes=allFive.openness,conciousnes=allFive.conciousness,extraversion=allFive.extraversion,agree=allFive.agree)
@app.route('/option2', methods=['POST','GET'])
def option2():
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
    req=request.form.get("option2")
    notEnd,allFive=m.setScore(req)
    if notEnd:
        return render_template('index.html' ,statement1=statement1 ,statement2=statement2, result=counter)
    else:
        return render_template("results.html", neuroticism=allFive.neuroticism,opennes=allFive.openness,conciousnes=allFive.conciousness,extraversion=allFive.extraversion,agree=allFive.agree)

@app.route('/results',methods=['GET'])
def scores():
     return render_template('results.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        m = Manager()
        m.reset_database()
        m.loadData()
    app.run()
