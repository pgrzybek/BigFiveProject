from random import Random
from BaseBigFive import BaseBigFive
from AllFive import AllFive
from dbInit import db


class Manager:
    def __init__(self):
        self.fileName = "Pytania.txt"

        self.dataRange= self.setRange()
    @staticmethod
    def stens(result, question_number):
        min_suma = -question_number
        max_suma = question_number
        # M = np.mean(wyniki)
        # SD = np.std(wyniki, ddof=1)
        #
        # # 🔹 3. Oblicz z-score i steny
        # z_scores = [(x - M) / SD for x in wyniki]
        # #z_scores = [np.sqrt((x - M)**2) / SD for x in wyniki]
        # steny = [round(z  + 3) for z in z_scores]
        sten = 1 + (result - min_suma) / (max_suma - min_suma) * 4
        # 🔹 4. Ogranicz wartości do 1–5
        sten = round(min(max(sten, 1), 5))
        return sten

    @staticmethod
    def reset_database():
        db.drop_all()
        db.create_all()
    @staticmethod
    def setRange():
        count = db.session.query(BaseBigFive).count()
        allID=[]
        for i in range(count):
            allID.append(i)
        return allID
    def getRandom(self):
        ids=self.dataRange
        random=Random()
        rvalue= -1
        if ids:
            rvalue=random.choice(ids)
            ids.remove(rvalue)

        # if ids:
        #     rvalue=random.choice(ids)
        #     ids.remove(rvalue)
        # else:
        #     rvalue=-1
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
        # query = db.session.query(AllFive).filter(AllFive.neuroticism.in_([1, -1])).all()
        # data=[]
        # for r in query:
        #     data.append(r.neuroticism)
        # print(data)
        # neuro=self.stens(data,3)
        # print(neuro)

        if score:
            scoreType=score.type
            opposite=score.opposite
            if opposite:
                match scoreType:
                    case "neuroticism":
                        allfive.neuroticism += 1
                        #allfive=AllFive(neuroticism=1)
                        #db.session.add(allfive)
                    case "extraversion":
                        allfive.extraversion += 1
                        #allfive=AllFive(extraversion=1)
                        #db.session.add(allfive)
                    case "openness":
                        #allfive=AllFive(openness=1)
                        #db.session.add(allfive)
                        allfive.openness += 1
                    case "agreeableness":
                        #allfive=AllFive(agree=1)
                        #db.session.add(allfive)
                        allfive.agreablesness += 1
                    case "conciousness":
                        #allfive=AllFive(conciousness=1)
                        #db.session.add(allfive)
                        allfive.conciousness += 1
            else:
                match scoreType:
                    case "neuroticism":
                        #allfive=AllFive(neuroticism=-1)
                        #db.session.add(allfive)
                        allfive.neuroticism -= 1
                    case "extraversion":
                        #allfive=AllFive(extraversion=-1)
                        #db.session.add(allfive)
                        allfive.extraversion -= 1
                    case "openness":
                        #allfive=AllFive(openness=-1)
                        #db.session.add(allfive)
                        allfive.openness -= 1
                    case "agreeableness":
                        #allfive=AllFive(agree=-1)
                        #db.session.add(allfive)
                        allfive.agreablesness -= 1
                    case "conciousness":
                        #allfive=AllFive(conciousness=-1)
                        #db.session.add(allfive)
                        allfive.conciousness += 1
        if not picked:

            # query = db.session.query(AllFive).filter(AllFive.neuroticism.in_([1, -1])).all()
            # data=[]
            # for r in query:
            #     data.append(r.neuroticism)
            # print(data)
            minMax = db.session.query(BaseBigFive).filter_by(type="neuroticism").count()

            allfive.neuroticism=self.stens(allfive.neuroticism,minMax)
            allfive.agreablesness=self.stens(allfive.agree,minMax)
            allfive.openness=self.stens(allfive.openness,minMax)
            allfive.conciousness=self.stens(allfive.conciousness,minMax)
            allfive.extraversion=self.stens(allfive.extraversion,minMax)
        db.session.commit()
        return picked,allfive

    def loadData(self):
        neuroticism = (db.session.query(BaseBigFive)
                       .filter_by(id=1)
                       .first())

        data = []
        with open(self.fileName, 'r', encoding='utf-8') as f:
            data = f.read().splitlines()

        if not neuroticism:
            allfive = AllFive(neuroticism=0, openness=0, conciousness=0, extraversion=0, agree=0, total=0)
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
                    fiveType = "agree"
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



# m = Manager()
# m.fileName = "Pytania.txt"
# print(m.loadData())
