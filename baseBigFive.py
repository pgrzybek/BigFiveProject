from dbInit import db


class BaseBigFive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    statement = db.Column(db.String)
    opposite = db.Column(db.Boolean,default=False)
    used= db.Column(db.Boolean,default=False)
    #allfive_id = db.Column(db.Integer, db.ForeignKey('allFive.id'))
    type= db.Column(db.String)



