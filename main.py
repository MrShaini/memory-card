from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from random import choice, shuffle
app = QApplication([])

from card_window import *
card_win.setWindowTitle("Memory Card")
card_win.resize(600, 500)
card_win.setLayout(card_layout)

class Question():

    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question 
        self.answer = answer 
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
        self.is_asking = True
        self.count_ask = 0
        self.count_right = 0


    def got_right(self, ):
        self.count_ask += 1
        self.count_right += 1

    def got_wrong(self):
        self.count_ask += 1 

q1 = Question("Ананас", "PineApple", "PuneApple", "PineAppel", "PineUpple")
q2 = Question("Міндастрі", "Mindustry", "Mindastry", "Mindestry", "Mindustri")
q3 = Question("Террарія", "Terraria", "Teraria", "Terarria", "Terariya")
q4 = Question("ти все вирішив?", "Майже", "ні", "так", "хто я?")
radio_buttons = [rbt1, rbt2, rbt3, rbt4]
questions = [q1, q2, q3, q4]

def  new_question():
    cur_quest = choice(questions)
    lbl_question.setText(cur_quest.question)
    lbl_result.setText(cur_quest.answer)

    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_quest.wrong_ans1)
    radio_buttons[1].setText(cur_quest.wrong_ans2)
    radio_buttons[2].setText(cur_quest.wrong_ans3)
    radio_buttons[3].setText(cur_quest.answer)


new_question()
card_win.show()
app.exec_()