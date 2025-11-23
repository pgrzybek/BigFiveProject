from dbInit import db


class AllFive(db.Model):
    __tablename__ = 'allFive'
    id = db.Column(db.Integer, primary_key=True)
    neurotiscm=db.Column(db.Integer)
    openness=db.Column(db.Integer)
    extraversion=db.Column(db.Integer)
    agreablesness=db.Column(db.Integer)
    conciousness=db.Column(db.Integer)
    Total=db.Column(db.Integer)
    # neuroticsm= db.relationship('Neuroticism', backref='allFive')
    # openness=db.relationship('Openness', backref='allFive')
    # extraversion=db.relationship('Extravert', backref='allFive')
    # agreablesness=db.relationship('Agreeableness', backref='allFive')
    # conciousness=db.relationship('Consciousness', backref='allFive')


