# import numpy as np
from asyncore import write
from string import ascii_uppercase, capwords
from sys import stdout
from shortcuts import intConvert, coloredText, color
from random import randint
import json

#[x] fill dict with combo's
#[ ] make 5 dice

def printScoreboard(passDict):
    if isinstance(passDict,dict):
        for x,y in passDict.items():
            stdout.write(f'{capwords(x)}: ')
            stdout.write(str(y)+'\n') if y > 0 else stdout.write('\n') #only writes score if there is a score
    else:
        print('passed object is not a dict')

def updateScore(value):
    scoreBoard = {
    "ones":0,
    "twos":0,
    "threes":0,
    "fours":0,
    "fives":0,
    "sixes":0,
    "three of a kind":0,
    "four of a kind":0,
    "full house":0,
    "small straight":0,
    "large straight":0,
    "chance":0,
    "yahtzee":0
    }

    for x,y in scoreBoard.items():
        print(f'{x}: {y}') if y > 0 else print(f'{x}:')

def createDice():
    diceDict = {}
    for i in range(5):
        diceString = f'dice {i+1}'
        diceDict.update({diceString:randint(1,6)})


if __name__ == '__main__':
    updateScore(1)