

from flask import Flask, render_template
from Manager import Manager
from AllFive import AllFive

from dbInit import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

@app.route('/', methods=['GET'])
def home( ):
    if m.getStatement():
        statement1=m.getStatement().statement
    else:
        statement1=" "
    return render_template('index.html',statement1=statement1)





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        m = Manager()
        m.loadData()
    app.run()
