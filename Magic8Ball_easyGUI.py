"""
Magic 8 - ball game. GUI

Implementing GUI for fun

"""

import random
from easygui import *

with open('answers.txt') as lines:
    # converting answers to a list
    answers = [i.strip() for i in lines]

while True:
    question = enterbox('Ask for a Yes or No question\nType quit to exit', '8-Ball')
    if question.lower() == 'quit':
        quit()
    else:
        # random choice/ ball shake - of answers 
        msgbox(random.choice(answers), 'Answer')
