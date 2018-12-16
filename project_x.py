import random
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot

# База неправильных глаголов
irregular = [
	{"form1": "beat", "form2": "beat", "form3": "beaten", "form_ing": "beating", "form_s": "beats"},
	{"form1": "become", "form2": "became", "form3": "become", "form_ing": "becoming", "form_s": "becomes"},
	{"form1": "begin", "form2": "began", "form3": "begun", "form_ing": "beginning", "form_s": "begins"},
	{"form1": "bend", "form2": "bent", "form3": "bent", "form_ing": "bending", "form_s": "bends"},
	{"form1": "bet", "form2": "bet", "form3": "bet", "form_ing": "betting", "form_s": "bets"},
	{"form1": "bite", "form2": "bit", "form3": "bitten", "form_ing": "biting", "form_s": "bites"},
	{"form1": "blow", "form2": "blew", "form3": "blown", "form_ing": "blowing", "form_s": "blows"},
	{"form1": "bring", "form2": "brought", "form3": "brought", "form_ing": "bringing", "form_s": "brings"},
	{"form1": "build", "form2": "built", "form3": "built", "form_ing": "building", "form_s": "builds"},
	{"form1": "buy", "form2": "bought", "form3": "bought", "form_ing": "buying", "form_s": "buys"},
	{"form1": "catch", "form2": "caught", "form3": "caught", "form_ing": "catching", "form_s": "catches"},
	{"form1": "choose", "form2": "chose", "form3": "chosen", "form_ing": "chosing", "form_s": "chooses"},
	{"form1": "come", "form2": "came", "form3": "come", "form_ing": "coming", "form_s": "comes"},
	{"form1": "cost", "form2": "cost", "form3": "cost", "form_ing": "costing", "form_s": "costs"},
	{"form1": "cut", "form2": "cut",  "form3": "cut", "form_ing": "cutting", "form_s": "cuts"},
	{"form1": "deal", "form2": "dealt", "form3": "dealt", "form_ing": "dealing", "form_s": "deals"},
	{"form1": "dig", "form2": "dug", "form3": "dug", "form_ing": "digging", "form_s": "digs"},
	{"form1": "do", "form2": "did", "form3": "done", "form_ing": "doing", "form_s": "does"},
	{"form1": "draw", "form2": "drew", "form3": "drawn", "form_ing": "drawing", "form_s": "draws"}]

# База правильных глаголов
regular = [
	{"form1": "ask", "form2": "", "form3": "", "form_ing": "asking", "form_s": "asks"},
	{"form1": "answer", "form2": "", "form3": "", "form_ing": "answering", "form_s": "answers"},
	{"form1": "allow", "form2": "", "form3": "", "form_ing": "allowing", "form_s": "allows"},
	{"form1": "borrow", "form2": "", "form3": "", "form_ing": "borrowing", "form_s": "borrows"},
	{"form1": "believe", "form2": "", "form3": "", "form_ing": "believing", "form_s": "believes"},
	{"form1": "cook", "form2": "", "form3": "", "form_ing": "cooking", "form_s": "cooks"},
	{"form1": "close", "form2": "", "form3": "", "form_ing": "closing", "form_s": "closes"},
	{"form1": "change", "form2": "", "form3": "", "form_ing": "changing", "form_s": "changes"},
	{"form1": "call", "form2": "", "form3": "", "form_ing": "calling", "form_s": "calls"},
	{"form1": "discuss", "form2": "", "form3": "", "form_ing": "discussing", "form_s": "discusses"},
	{"form1": "explain", "form2": "", "form3": "", "form_ing": "explaining", "form_s": "explains"},
	{"form1": "finish", "form2": "", "form3": "", "form_ing": "finishing", "form_s": "finishes"},
	{"form1": "play", "form2": "", "form3": "", "form_ing": "playing", "form_s": "plays"},
	{"form1": "move", "form2": "", "form3": "", "form_ing": "moving", "form_s": "moves"},
	{"form1": "manage", "form2": "", "form3": "", "form_ing": "managing", "form_s": "manages"},
	{"form1": "suggest", "form2": "", "form3": "", "form_ing": "suggesting", "form_s": "suggests"}]

for i in regular:
    if i["form1"][-1] == "e":
        i["form2"] = i["form1"] + "d"
    else:
        i["form2"] = i["form1"] + "ed"
    i["form3"] = i["form2"]
  
# Список всех глаголов
all_verbs = regular + irregular

# Список местоимений
pronouns = ["I", "you", "he", "she", "it", "we", "they"]

# Список (словарь) типов предложений и их символьных обозначений
sentense_types = [["plus", "+"], ["minus", "–"], ["question", "?"]]

# Список типов времен английского глагола. Каждый элемент состоит из tense1 (Future, Present, Past) и  tense2 (Simple, Continuous, Perfect, Perfect Continuous)
tense_types = [["Present", "Simple"],
               ["Present", "Continuous"],
               ["Present", "Perfect"],
               ["Present", "Perfect Continuous"],
               ["Past", "Simple"],
               ["Past", "Continuous"],
               ["Past", "Perfect"],
               ["Past", "Perfect Continuous"],
               ["Future", "Simple"],
               ["Future", "Continuous"],
               ["Future", "Perfect"],
               ["Future", "Perfect Continuous"]]

# Список пользовательских предложений. Сюда добавляются элементы, содержащие правильное предложение, пользовательское предложение, статус правильно / неправильно
user_sentenses = []

# Функция, возвращающая рандомное число из промежутка mymin — mymax.
def getRandomInt(mymin, mymax):
    return random.randint(mymin, mymax)

# Создание правильного предложения
def makeRightSentense(tense1, tense2, pronoun, verb, verb2, verb3, verb_ing, verb_s, sentenseType, sentenseTypeName, beForm, doForm, haveForm):
    rightSentense = ""
    if tense1 == "Present":
        if pronoun == "I":
            if sentenseTypeName == "minus":
                beForm = "am not"
            else:
                beForm = "am"   
        elif pronoun == "you" or pronoun == "we" or pronoun == "they":
            if sentenseTypeName == "minus":
                beForm = "are not"
            else:
                beForm = "are"
            
        elif pronoun == "he" or pronoun == "she" or pronoun == "it":
            if sentenseTypeName == "minus":
                beForm = "is not"
            else:
                beForm = "is"
    if tense1 == "Past":
        if pronoun == "you" or pronoun == "we" or pronoun == "they":
            if sentenseTypeName == "minus":
                beForm = "were not"
            else:
                beForm = "were"
            
        elif pronoun == "I" or pronoun == "he" or pronoun == "she" or pronoun == "it":
            if sentenseTypeName == "minus":
                beForm = "was not"
            else:
                beForm = "was"
    if tense1 == "Future":   
        beForm = "be"
    if tense1 == "Present":  
        if pronoun == "I" or pronoun == "you" or pronoun == "we" or pronoun == "they":
            if sentenseTypeName == "minus":
                doForm = "do not"
            else:
                doForm = "do" 
        elif pronoun == "he" or pronoun == "she" or pronoun == "it":
            if sentenseTypeName == "minus":
                doForm = "does not"
            else:
                doForm = "does"
    elif tense1 == "Past":
        if sentenseTypeName == "minus":
            doForm = "did not"
        else:
            doForm = "did"     
    if pronoun == "he" or pronoun == "she" or pronoun == "it":
        if sentenseTypeName == "minus":
            haveForm = "has not"
        else:
            haveForm = "has"
    elif pronoun == "I" or pronoun == "we" or pronoun == "you" or pronoun == "they":
        if sentenseTypeName == "minus":
            haveForm = "have not"
        else:
            haveForm = "have"
            
    # Основная часть
    if sentenseTypeName == "plus":
        if tense1 == "Present":
            if tense2 == "Simple":
                if pronoun == "he" or pronoun == "she" or pronoun == "it":
                    rightSentense = pronoun + " " + verb_s + "."
                else:
                    rightSentense = pronoun + " " + verb + "."    
            elif tense2 == "Continuous":
                rightSentense = pronoun + " " + beForm + " " + verb_ing + "."
            elif tense2 == "Perfect":
                rightSentense = pronoun + " " + haveForm + " " + verb3 + "."
            elif tense2 == "Perfect Continuous":
                rightSentense = pronoun + " " + haveForm + " " + "been" + " " + verb_ing + "." 
        elif tense1 == "Past":
            if tense2 == "Simple":
                rightSentense = pronoun + " " + verb2 + "."    
            elif tense2 == "Continuous":
                rightSentense = pronoun + " " + beForm + " " + verb_ing + "."
            elif tense2 == "Perfect":
                rightSentense = pronoun + " " + "had" + " " + verb3 + "."
            elif tense2 == "Perfect Continuous":
                rightSentense = pronoun + " " + "had" + " " + "been" + " " + verb_ing + "."
        elif tense1 == "Future":
            if tense2 == "Simple":
                rightSentense = pronoun + " " + "will" + " " + verb + "."  
            elif tense2 == "Continuous":
                rightSentense = pronoun + " " + "will" + " " + beForm + " " + verb_ing + "."
            elif tense2 == "Perfect":
                rightSentense = pronoun + " " + "will" + " " + "have" + " " + verb3 + "."
            elif tense2 == "Perfect Continuous":
                rightSentense = pronoun + " " + "will" + " " + "have" + " " + "been" + " " + verb_ing + "."
    elif sentenseTypeName == "minus":
        if tense1 == "Present":
            if tense2 == "Simple":
                rightSentense = pronoun + " " + doForm + " " + verb + "."  
            elif tense2 == "Continuous":
                rightSentense = pronoun + " " + beForm + " " + verb_ing + "."
            elif tense2 == "Perfect":
                rightSentense = pronoun + " " + haveForm + " " + verb3 + "."
            elif tense2 == "Perfect Continuous":
                rightSentense = pronoun + " " + haveForm + " " + "been" + " " + verb_ing + "."   
        elif tense1 == "Past":
            if tense2 == "Simple":
                rightSentense = pronoun + " " + doForm + " " + verb + "."  
            elif tense2 == "Continuous":
                rightSentense = pronoun + " " + beForm + " " + verb_ing + "."
            elif tense2 == "Perfect":
                rightSentense = pronoun + " " + "had" + " " + "not" + " " + verb3 + "."
            elif tense2 == "Perfect Continuous":
                rightSentense = pronoun + " " + "had" + " " + "not" + " " + "been" + " " + verb_ing + "."
        elif tense1 == "Future":
            if tense2 == "Simple":
                rightSentense = pronoun + " " + "will" + " " + "not" + " " + verb + "."    
            elif tense2 == "Continuous":
                rightSentense = pronoun + " " + "will" + " " + "not" + " " + beForm + " " + verb_ing + "."
            elif tense2 == "Perfect":
                rightSentense = pronoun + " " + "will" + " " + "not" + " " + "have" + " " + verb3 + "."
            elif tense2 == "Perfect Continuous":
                rightSentense = pronoun + " " + "will" + " " + "not" + " " + "have" + " " + "been" + " " + verb_ing + "."
    elif sentenseTypeName == "question":
        if tense1 == "Present":
            if tense2 == "Simple":
                rightSentense = doForm + " " + pronoun + " " + verb + "?"
            elif tense2 == "Continuous":
                rightSentense = beForm + " " + pronoun + " " + verb_ing + "?"
            elif tense2 == "Perfect":
                rightSentense = "have" + " " + pronoun + " " + verb3 + "?"
            elif tense2 == "Perfect Continuous":
                rightSentense = haveForm + " " + pronoun + " " + "been" + " " + verb_ing + "?"
        elif tense1 == "Past":
            if tense2 == "Simple":
                rightSentense = doForm + " " + pronoun + " " + verb + "?"  
            elif tense2 == "Continuous":
                rightSentense = beForm + " " + pronoun + " " + verb_ing + "?"
            elif tense2 == "Perfect":
                rightSentense = "had" + " "+  pronoun + " " + verb3 + "?"
            elif tense2 == "Perfect Continuous":
                rightSentense = "had" + " " + pronoun + " " + "been" + " " + verb_ing + "?"
        elif tense1 == "Future":
            if tense2 == "Simple":
                rightSentense = "will" + " " + pronoun + " " + verb + "?"  
            elif tense2 == "Continuous":
                rightSentense = "will" + " " + pronoun + " " + beForm + " " + verb_ing + "?"
            elif tense2 == "Perfect":
                rightSentense = "will" + " " + pronoun + " " + "have" + " " + verb3 + "?"
            elif tense2 == "Perfect Continuous":
                rightSentense = "will" + " " + pronoun + " " + "have" + " " + "been" + " " + verb_ing + "?"
    return rightSentense

# Проверка правильности предложения
def check_sentense(user_sentense, right_sentense):
    right_sentense_lower = right_sentense.replace(".", "")
    right_sentense_lower = right_sentense_lower.lower()
    replaced = user_sentense.lower()
    for i in range(5):
        replaced = replaced.replace("  ", " ")
    replaced = replaced.replace("I'm", "I am")
    replaced = replaced.replace("you're", "you are")
    replaced = replaced.replace("he's", "he is")
    replaced = replaced.replace("she's", "she is")
    replaced = replaced.replace("it's", "it is")
    replaced = replaced.replace("we're", "we are")
    replaced = replaced.replace("they're", "they are")
    replaced = replaced.replace("isn't", "is not")
    replaced = replaced.replace("aren't", "are not")
    replaced = replaced.replace("doesn't", "does not")
    replaced = replaced.replace("don't", "do not")
    replaced = replaced.replace("wasn't", "was not")
    replaced = replaced.replace("weren't", "were not")
    replaced = replaced.replace("didn't", "did not")
    replaced = replaced.replace("hasn't", "has not")
    replaced = replaced.replace("haven't", "have not")
    replaced = replaced.replace("hadn't", "had not")
    replaced = replaced.replace("'ll", " will")
    replaced = replaced.replace("won't", "will not")
    replaced = replaced.replace(".", "")
    replaced = replaced.strip()
    success = replaced == right_sentense_lower
    return success

exes_number = 10

for i in range(exes_number):
    tense = tense_types[getRandomInt(0, len(tense_types) - 1)]
    verb = all_verbs[getRandomInt(0, len(all_verbs) - 1)]
    pronoun = pronouns[getRandomInt(0, len(pronouns) - 1)]
    sentense_type = sentense_types[getRandomInt(0, len(sentense_types) - 1)]
    correct_sentense = makeRightSentense(tense[0], tense[1], pronoun, verb["form1"], verb["form2"], verb["form3"], verb["form_ing"], verb["form_s"], sentense_type[1], sentense_type[0], "", "", "")
    print(tense[0], tense[1], pronoun, verb["form1"], sentense_type[1])
    user_sentense = input()
    user_sentenses.append([user_sentense, sentense_type, tense, correct_sentense, check_sentense(user_sentense, correct_sentense)])

    
# Создание таблицы результатов
class table(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 500
        self.initUI()
 
    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createTable()
 
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
 
        self.show()
 
    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(exes_number)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Время", "Ваше предложение", "Правильное предложение"])
        for i in range(len(user_sentenses)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(" ".join(user_sentenses[i][2])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(user_sentenses[i][0]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(user_sentenses[i][3].capitalize()))
            for j in range(3):
                if user_sentenses[i][-1]:
                    self.tableWidget.item(i, j).setBackground(QColor(0, 255, 0))
                else:
                    self.tableWidget.item(i, j).setBackground(QColor(250, 0, 0))
        self.tableWidget.move(20, 20)
        self.tableWidget.resizeColumnsToContents()
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = table()
    sys.exit(app.exec_())



