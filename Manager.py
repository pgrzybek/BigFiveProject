from random import Random
from BaseBigFive import BaseBigFive
from AllFive import AllFive
from dbInit import db


class Manager:
    def __init__(self):
        self.fileName = "Pytania.txt"

        self.dataRange= self.setRange()

    @staticmethod
    def reset_database():
        db.drop_all()
        db.create_all()

    def setRange(self):
        count = db.session.query(BaseBigFive).count()
        allID=[]
        for i in range(count):
            allID.append(i)
        return allID
    def getRandom(self):
        ids=self.dataRange
        random=Random()
        if ids:
            rvalue=random.choice(ids)
            ids.remove(rvalue)
        else:
            rvalue=-1
        return rvalue

    def getStatement(self):
        idPicked=self.getRandom()
        if not idPicked==-1:
            picked = db.session.query(BaseBigFive).filter_by(id=idPicked).first()
        else:
            picked=None
        return picked

    def setScore(self, picked):
        allfive = db.session.query(AllFive).filter_by(id=1).first()
        score= db.session.query(BaseBigFive).filter_by(statement=picked).first()
        if score:
            scoreType=score.type
            opposite=score.opposite
            if opposite:
                match scoreType:
                    case "neuroticism":
                        allfive.neuroticism += 1
                    case "extraversion":
                        allfive.extraversion += 1
                    case "openness":
                        allfive.openness += 1
                    case "agreeableness":
                        allfive.agreablesness += 1
                    case "conciousness":
                        allfive.conciousness += 1
            else:
                match scoreType:
                    case "neuroticism":
                        allfive.neuroticism -= 1
                    case "extraversion":
                        allfive.extraversion -= 1
                    case "openness":
                        allfive.openness -= 1
                    case "agreeableness":
                        allfive.agreablesness -= 1
                    case "conciousness":
                        allfive.conciousness += 1
        db.session.commit()
        return allfive

    def loadData(self):
        neuroticism = (db.session.query(BaseBigFive)
                       .filter_by(id=1)
                       .first())

        data = []
        with open(self.fileName, 'r', encoding='utf-8') as f:
            data = f.read().splitlines()

        if not neuroticism:
            allfive = AllFive(neuroticism=0, openness=0, conciousness=0, extraversion=0, agreablesness=0, total=0)
            db.session.add(allfive)
            i = 0
            fiveType = ""
            opposite = False
            while i < len(data):
                if data[i] == 'Neurotyczność':
                    i = i + 1
                    fiveType = "neuroticism"
                if data[i] == "Stwierdzenia":
                    i = i + 1
                    opposite = False
                if data[i] == "Odwrotne":
                    i = i + 1
                    opposite = True
                if data[i] == 'Ekstrawersja':
                    i = i + 1
                    fiveType = "extraversion"
                if data[i] == "Stwierdzenia":
                    i = i + 1
                    opposite = False
                if data[i] == "Odwrotne":
                    i = i + 1
                    opposite = True
                if data[i] == 'Otwartość':
                    i = i + 1
                    fiveType = "openness"
                if data[i] == "Stwierdzenia":
                    i = i + 1
                    opposite = False
                if data[i] == "Odwrotne":
                    i = i + 1
                    opposite = True
                if data[i] == 'Ugodowość':
                    i = i + 1
                    fiveType = "agreeableness"
                if data[i] == "Stwierdzenia":
                    i = i + 1
                    opposite = False
                if data[i] == "Odwrotne":
                    i = i + 1
                    opposite = True
                if data[i] == 'Sumienność':
                    i = i + 1
                    fiveType = "conciousness"
                if data[i] == "Stwierdzenia":
                    i = i + 1
                    opposite = False
                if data[i] == "Odwrotne":
                    i = i + 1
                    opposite = True
                baseType = BaseBigFive(statement=data[i], type=fiveType, opposite=opposite)
                db.session.add(baseType)
                i = i + 1
            db.session.commit()
        return []

    def addData(self, data, i):

        statement = []
        opossite = []

        while data[i] != 'Odwrotne':
            if data[i] == 'Stwierdzenia':
                i = i + 1
            statement.append(data[i])
            i += 1
            if not data:
                break
        if data[i] == "Odwrotne":
            i = 0
            while data != "Koniec" or data != ' ':
                opossite.append(data[i])
                i += 1
                if not data:
                    break
        return statement, opossite

# m = Manager()
# m.fileName = "Pytania.txt"
# print(m.loadData())
