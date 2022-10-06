

'''
Magic 8 - ball game. GUI

The aim of this exercise is to use a proper file handling method.
Automatically closing it after use
Also to practice implementing GUI for fun

'''

import random
from easygui import*


# with and the open function the file will be autom. closed
with open('answers.txt') as lines
    # converting answers to a list
    answers = [i.strip() for i in lines]

while True:
    # question and if quit 
    question = enterbox('Ask for a Yes or No question\nType quit to exit', '8-Ball')
    if question.lower() == 'quit':
        quit()
    else:
        # random choice/ ball shake - of answers 
        msgbox(random.choice(answers), 'Answer')
