from flask import Flask, render_template, request,g
from manager import Manager
from dbInit import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
counter=1
#m = Manager()

def get_manager():
    if 'manager' not in g:
        g.manager = Manager()
        g.manager.reset_database()
        g.manager.loadData()
    return g.manager

with app.app_context():
    db.create_all()
    g.manager.loadData()
    # m = Manager()
    # m.reset_database()
    # m.loadData()

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
    m = get_manager()
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
    notEnd,allfive,minMax=m.setScore(req)
    if notEnd and statement1!="" and statement2!="":
        return render_template("index.html" ,statement1=statement1 ,statement2=statement2,result=counter)
    else:
        m.reset()
        allfive.neuroticism = m.stens(allfive.neuroticism, minMax)
        allfive.agreablesness = m.stens(allfive.agree, minMax)
        allfive.openness = m.stens(allfive.openness, minMax)
        allfive.conciousness = m.stens(allfive.conciousness, minMax)
        allfive.extraversion = m.stens(allfive.extraversion, minMax)
        #print(allfive.neuroticism,allfive.openness,allfive.conciousness,allfive.extraversion,allfive.agree)
        neuroticism=m.addStars(allfive.neuroticism)
        agree=m.addStars(allfive.agree)
        opennes=m.addStars(allfive.openness)
        concious=m.addStars(allfive.conciousness)
        extraversion=m.addStars(allfive.extraversion)


        return render_template("results.html", neuroticism=neuroticism,opennes=opennes,conciousnes=concious,extraversion=extraversion,agree=agree)

@app.route('/option2', methods=['POST','GET'])
def option2():
    global counter
    counter += 1
    m = get_manager()
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
    notEnd,allfive,minMax=m.setScore(req)
    if notEnd and statement1!="" and statement2!="":
        return render_template('index.html' ,statement1=statement1 ,statement2=statement2, result=counter)
    else:
        m.reset()
        allfive.neuroticism = m.stens(allfive.neuroticism, minMax)
        allfive.agreablesness = m.stens(allfive.agree, minMax)
        allfive.openness = m.stens(allfive.openness, minMax)
        allfive.conciousness = m.stens(allfive.conciousness, minMax)
        allfive.extraversion = m.stens(allfive.extraversion, minMax)
        neuroticism=m.addStars(allfive.neuroticism)
        agree=m.addStars(allfive.agree)
        openness=m.addStars(allfive.openness)
        conciousness=m.addStars(allfive.conciousness)
        extraversion=m.addStars(allfive.extraversion)
        print(allfive.neuroticism,allfive.openness,allfive.conciousness,allfive.extraversion,allfive.agree)

        return render_template("results.html", neuroticism=neuroticism,opennes=openness,conciousnes=conciousness,extraversion=extraversion,agree=agree)

@app.route('/results',methods=['GET'])
def scores():
     return render_template('results.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        m = Manager()
        m.reset_database()
        m.loadData()
    app.run(port=8080)
