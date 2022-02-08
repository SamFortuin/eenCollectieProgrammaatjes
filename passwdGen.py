from string import ascii_lowercase, ascii_uppercase
from random import randint, choice, shuffle
from shortcuts import intConvert,coloredText,color
from sys import stdout


def addScpecialChars(outList, debug):
    #adds 3 special chars
    specialChars = ['@','#','$','%','&','_','?']
    for i in range(3):
        outList.append(choice(specialChars))
    if debug:
        stdout.write(coloredText('',color.PURPLE,'Chars in passwd: '))
        stdout.write('3 Special, ')
    
def addUpperCase(outList, debug):
    #adds between 2 and 6 upper case chars
    randNum = randint(2,6)
    for i in range(randNum):
        outList.append(choice(ascii_uppercase))
    if debug:
        stdout.write(f'{randNum} Upper, ')

def addNumbers(outList, debug):
    #adds between 4 and 7 numbers
    nums = list(range(10))
    randNum = randint(4,7)
    for i in range(randNum):
        outList.append(choice(nums))
    if debug:
        stdout.write(f'{randNum} Numbers, ')

def addLowerCase(outList, debug):
    remaining = 20-len(outList)
    for i in range(remaining):
        outList.append(choice(ascii_lowercase))
    if debug:
        stdout.write(f'{remaining+4} Lower:\n')

def createPasswd(debug):
    inList = [] #creates blank list
    addScpecialChars(inList,debug)
    addUpperCase(inList,debug)
    addNumbers(inList,debug)
    addLowerCase(inList,debug)

    for x in range(randint(1,10)):
        shuffle(inList)

    for i in range(3):
        inList.insert(0,choice(ascii_lowercase))
    inList.append(choice(ascii_lowercase))

    return inList

def main(debug=False,numbered=True):
    mainList = []
    amount = intConvert(input('hoeveel wachtwoorden wilt u?\n'))
    if isinstance(amount,int) and amount > 0:
        s = '' if amount < 2 else 's'
        print(coloredText('\n', color.YELLOW, f'generated password{s}:'))
        for i in range(amount):
            mainList.append(createPasswd(debug))
            if numbered:
                mainList[i].insert(0,f'{i+1}. ')
            if debug:
                mainList[i].append("\n")
            print(*mainList[i],sep='')
    else:
        print('invalid input')
        main()

# main(debug=True)
main()


#[ ] implement json functions for fun
#[ ] with json also make txt that that makes it so that a newly genned file's name is one more than the previous file
#[ ] when json remove the numbers 