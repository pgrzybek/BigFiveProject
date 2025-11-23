from BaseBigFive import BaseBigFive
from BigFiveEntities import Neuroticism, Extravert, Openness, Agreeableness, Consciousness
from AllFive import  AllFive
from dbInit import db


class Manager:
    def __init__(self):
        self.fileName = ""
        self.picked=""
    def getStatement(self):
        self.picked=db.session.query(Neuroticism).filter_by(id=1).first()
        return self.picked

    def setScore(self,type):
        allfive=db.session.query(AllFive).filter_by(id=1).first()
        match type:
            case "neurotism":
                allfive.neurotycznosc=+1
            case "extravert":
                allfive.extravert=+1
            case "openness":
                allfive.openness=+1
            case "agreeableness":
                allfive.agreeablenes=+1
            case "conciousness":
                allfive.conciousness=+1





    def loadData(self):
        neuroticism = (db.session.query(BaseBigFive)
                   .filter_by(id=1)
                   .first())
        if not neuroticism:
            allfive=AllFive(neuroticism=0,openness=0,conciousness=0,extravert=0,agreablesness=0,total=0)
            db.session.add(allfive)

            neuroticism=BaseBigFive(statement="Często łatwo się stresuję",type="neurotism")
            db.session.add(neuroticism)
            neuroticism=BaseBigFive(statement="Mam tendencję do zamartwiania się.",type="neurotism")
            db.session.add(neuroticism)
            neuroticism=BaseBigFive(statement="Trudno mi utrzymać spokój w trudnych sytuacjach",type="neurotism")
            db.session.add(neuroticism)

            db.session.commit()
        # data = []
        # with open(self.fileName, 'r', encoding='utf-8') as f:
        #     data = f.read().splitlines()
        #

        # i=0
        # while i < len(data):
        #     if data[i] == 'Neurotyczność':
        #         i=i+1
        #
        #         statement,oposite=self.addData(data[i],i)
        #         neuroticism=Neuroticism(statement=statement)
        #         db.session.add(neuroticism)
        #     if data[i] == 'Ekstrawersja':
        #         i=i+1
        #         statement,oposite=self.addData(data[i],i)
        #         extrawert=Extravert(statement=statement)
        #         db.session.add(extrawert)
        #     if data[i] == 'Otwartość':
        #         i=i+1
        #         statement,oposite=self.addData(data[i],i)
        #         openness=Openness(statement=statement)
        #         db.session.add(openness)
        #     if data[i] == 'Ugodowość':
        #         i=i+1
        #         statement,oposite=self.addData(data[i],i)
        #         agreablesness=Agreeableness(statement=statement)
        #         db.session.add(agreablesness)
        #     if data[i] == 'Sumienność':
        #         i=i+1
        #         statement,oposite=self.addData(data[i],i)
        #         concis=Conciseness(statement=statement)
        #         db.session.add(concis)
        #     i=i+1
        return []

    def addData(self, data,i):

        statement = []
        opossite = []

        while data[i] != 'Odwrotne':
            if data[i] == 'Stwierdzenia':
                i=i+1
            statement.append(data[i])
            i += 1
            if not data:
                break
        if data[i] == "Odwrotne":
            i = 0
            while data != "Koniec" or data!= ' ':
                opossite.append(data[i])
                i += 1
                if not data:
                    break
        return statement, opossite



# m = Manager()
# m.fileName = "Pytania.txt"
# print(m.loadData())
