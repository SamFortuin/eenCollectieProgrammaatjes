from ast import Num
from asyncore import write
from string import ascii_uppercase, capwords
from sys import stdout
from shortcuts import intConvert, coloredText, color
from random import randint

#[X] fill dict with combo's
#[X] make 5 dice

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

def fancyDice(*inDice):
    #[ ]zero base dict so the +1 in the write isn't needed anymore
    diceDict = {
    1:{1:' ------- ',2:' ------- ',3:' ------- ',4:' ------- ',5:' ------- ',6:' ------- '},
    2:{1:'|       |',2:'| o     |',3:'| o     |',4:'| o   o |',5:'| o   o |',6:'| o   o |'},
    3:{1:'|   o   |',2:'|       |',3:'|   o   |',4:'|       |',5:'|   o   |',6:'| o   o |'},
    4:{1:'|       |',2:'|     o |',3:'|     o |',4:'| o   o |',5:'| o   o |',6:'| o   o |'},
    5:{1:' ------- ',2:' ------- ',3:' ------- ',4:' ------- ',5:' ------- ',6:' ------- '}
    }

    for i in range(5): #5 is for the 5 lines that de dice art requires
        for args in inDice:
            stdout.write(diceDict[i+1][args])#writes the current line (i) of the passed in dice value
            stdout.write('   ')
        stdout.write('\n')

def displayScore(scoreBoardIn):
    for x,y in scoreBoardIn.items():    
        print(f'{x}: {y}') if y > 0 else print(f'{x}:')

def printScoreboard(passDict):
    if isinstance(passDict,dict):
        for x,y in passDict.items():
            stdout.write(f'{capwords(x)}: ')
            stdout.write(str(y)+'\n') if y > 0 else stdout.write('\n') #only writes score if there is a score
    else:
        print('passed object is not a dict')


def rollDice(num):
    diceList = []
    for i in range(num):
        diceList.append(randint(1,6))
    return diceList

def main():
    pass

if __name__ == '__main__':
    a = rollDice(5)
    # a = [1,2,3,4,5,6]
    fancyDice(*a)