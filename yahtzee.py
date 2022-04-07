from string import ascii_uppercase, capwords
from sys import stdout
from shortcuts import intConvert, coloredText, color, clearScreen
from random import randint
from os import system

scoreBoard = {
    "ones":0,
    "twos":0,
    "threes":1,
    "fours":1,
    "fives":1,
    "sixes":1
}

def fancyDice(*inDice):
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
    r'''#!old code
    loopNum = 0
    while loopNum < 3:
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
        
        y = 0
        for x in keptList:
            if isinstance(x,int):
                y += 1
            # elif 
        if y == len(keptList):
            loopNum+=1
        else:
            print('a')
        clearScreen(0.1)
    print(hand)
    '''
    hand = []
    nextRoll = True
    # for i in range(1):
    for i in range(3):#3 for the three dice throws
        rolledDice = rollDice(5-len(hand))
        print('Rolled dice')
        fancyDice(*rolledDice)
        while True:
            if len(hand) > 0:
                print('Your dice')
                fancyDice(*hand)
            keep = input('\nWhich dice do you want to keep?\n').replace(' ','')
            if keep != "":
                keep = keep.split(',')
                for x in keep:
                    try:
                        indexDice = keep.index(x)
                        keep[indexDice] = int(x)
                        nextRoll = True
                    except ValueError:
                        print('invalid input')
                        nextRoll = False
                        break
            if not nextRoll:
                continue
            for x in keep:
                hand.append(x)
            break
    system('cls')
    print("you have:")
    combos = []
    for i in range(6):
        combos.append(f'{hand.count(i+1)}x {i+1}') if hand.count(i+1) > 0 else None
    print(*combos,sep='\n')
    while True:
        comboAppend = input("Which dice do you want to add to the scoreboard?\n")
        try:
            comboAppend = int(comboAppend)
            if comboAppend in keep:
                print(f'added to {comboAppend}')
                translateionDict = {1:'ones',2:'twos',3:'threes',4:'fours',5:'fives',6:'sixes'}
                scoreBoard[translateionDict[comboAppend]] = comboAppend*hand.count(comboAppend)
            else:
                print('not possible to add to scoreboard')
                continue
        except ValueError:
            print("not a number")
            continue
        break


if __name__ == '__main__':
    while True:
        scoreCheck = list(scoreBoard.values())
        while 0 in scoreCheck:
            print(scoreCheck)
            gameLoop()
            scoreCheck = list(scoreBoard.values())
        else:
            print("Your score:")
            for x,y in scoreBoard.items():
                 print(f'{x}:   {y} points') if x == 'ones' or x == 'twos' else (print(f'{x}: {y} points') if x == 'threes' else print(f'{x}:  {y} points'))
            print(f'Total:  {sum(list(scoreBoard.values()))} points')
            break