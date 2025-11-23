from dbInit import db


class AllFive(db.Model):
    __tablename__ = 'allFive'
    id = db.Column(db.Integer, primary_key=True)
    neuroticsm= db.relationship('Neuroticism', backref='allFive')
    openness=db.relationship('Openness', backref='allFive')
    extraversion=db.relationship('Extravert', backref='allFive')
    agreablesness=db.relationship('Agreeableness', backref='allFive')
    conciousness=db.relationship('Consciousness', backref='allFive')


