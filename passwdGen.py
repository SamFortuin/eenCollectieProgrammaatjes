from string import ascii_lowercase,ascii_uppercase
from random import randint, choice, shuffle
from shortcuts import intConvert,coloredText,color


def addScpecialChars(outList, debug):
    #adds 3 special chars
    specialChars = ['@','#','$','%','&','_','?']
    for i in range(3):
        outList.append(choice(specialChars))
    
def addUpperCase(outList, debug):
    #adds between 2 and 6 upper case chars
    for i in range(randint(2,6)):
        outList.append(choice(ascii_uppercase))

def addNumbers(outList, debug):
    #adds between 4 and 7 numbers
    nums = list(range(10))
    for i in range(randint(4,7)):
        outList.append(choice(nums))

def addLowerCase(outList, debug):
    for i in range(20-len(outList)):
        outList.append(choice(ascii_lowercase))

def createPasswd(inList, debug):
    passwdList,inList = [],[]
    addScpecialChars(inList,debug)
    addUpperCase(inList,debug)
    addNumbers(inList,debug)
    addLowerCase(inList,debug)

    for i in range(choice(list(range(10)))):
        shuffle(inList)

    for i in range(3):
        inList.insert(0,choice(ascii_lowercase))
    inList.append(choice(ascii_lowercase))

    outlist = inList
    return outlist


def main(numbered=True, debug=False):
    mainList,temp = [],[]
    amount = intConvert(input('hoeveel wachtwoorden wilt u?\n'))
    if isinstance(amount,int) and amount > 0:
        s = '' if amount < 2 else 's'
        print(coloredText('\n', color.YELLOW, f'generated password{s}:'))
        for i in range(amount):
            mainList.append(createPasswd(temp,debug))
            if numbered:
                mainList[i].insert(0,f'{i+1}. ')
            print(*mainList[i],sep='')
    else:
        print('invalid input')
        main()

main()