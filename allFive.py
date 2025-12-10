from dbInit import db


class AllFive(db.Model):
    __tablename__ = 'allFive'
    id = db.Column(db.Integer, primary_key=True)
    neuroticism=db.Column(db.Integer)
    openness=db.Column(db.Integer)
    extraversion=db.Column(db.Integer)
    agree=db.Column(db.Integer)
    conciousness=db.Column(db.Integer)
    total=db.Column(db.Integer)
    # neuroticsm= db.relationship('Neuroticism', backref='allFive')
    # openness=db.relationship('Openness', backref='allFive')
    # extraversion=db.relationship('Extravert', backref='allFive')
    # agreablesness=db.relationship('Agreeableness', backref='allFive')
    # conciousness=db.relationship('Consciousness', backref='allFive')


