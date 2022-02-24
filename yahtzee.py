from string import ascii_uppercase, capwords
from sys import stdout
from shortcuts import intConvert, coloredText, color, clearScreen
from random import randint
from os import system

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
    #[X]zero base dict so the +1 in the write isn't needed anymore
    diceDict = {
        0:{1:' ------- ',2:' ------- ',3:' ------- ',4:' ------- ',5:' ------- ',6:' ------- '},
        1:{1:'|       |',2:'| o     |',3:'| o     |',4:'| o   o |',5:'| o   o |',6:'| o   o |'},
        2:{1:'|   o   |',2:'|       |',3:'|   o   |',4:'|       |',5:'|   o   |',6:'| o   o |'},
        3:{1:'|       |',2:'|     o |',3:'|     o |',4:'| o   o |',5:'| o   o |',6:'| o   o |'},
        4:{1:' ------- ',2:' ------- ',3:' ------- ',4:' ------- ',5:' ------- ',6:' ------- '}
    }

    for i in range(5): #5 is for the 5 lines that de dice art requires
        for args in inDice:
            stdout.write(diceDict[i][args])#writes the current line (i) of the passed in dice value
            stdout.write('     ')
        stdout.write('\n')

def displayScore(scoreBoardIn):
    for x,y in scoreBoardIn.items():
        print(f'{capwords(x)}: {y}') if y > 0 else print(f'{capwords(x)}:')

def rollDice(num):
    diceList = []
    for i in range(num):
        diceList.append(randint(1,6))
    return diceList
   

def gameLoop():
    hand = []
    i = 0
    while i < 3:
        # fancyDice(1,2,3,4,5,6) # test dice
        a = rollDice(5-len(hand))
        print('rolled dice:')
        fancyDice(*a)
        if len(hand) > 0:
            print('\ndice in hand:')
            fancyDice(*hand)
        keepDice = input('\nwhich dice do you want to keep?\n')

        keptList = keepDice.replace(' ','').split(',')

        for x in keptList:
            if x.isdigit() and int(x) < 7 and int(x) > 0:
                indexList = keptList.index(x)
                keptList[indexList] = int(x)
                hand.append(keptList[indexList])
            else:
                print('invalid')
        i+=1
        clearScreen(0.1)
        # print(hand)
    print(hand)

if __name__ == '__main__':
    gameLoop()