from string import ascii_lowercase,ascii_uppercase
from random import randint, shuffle

def intConvert(num):
    numConvert1 = False
    numConvert2 = True
    alphabet = list(ascii_lowercase) #creates list of lowercase alphabet
    for i in range(10):
        if str(i) in num:
            numConvert1 = True
    for x in range(26):
        if alphabet[x] in num: #checks if a letter is present in the arg
            numConvert2 = False
    if numConvert1 and numConvert2: #skips == True because of if logic
        return int(num)
    else:
        return num

def addScpecialChars():
    global todo, outlist, specialChars
    specialChars = ['@','#','$','%','&','_','?']
    for i in range(3):
        outList.append(specialChars[randint(0,6)])
        todo -= 1

def addUpperCase():
    global todo, outList
    upperCase = list(ascii_uppercase)
    for i in range(randint(2,6)):
        outList.append(upperCase[randint(0,25)])
        todo -= 1

def addNumbers():
    global todo, outList, nums
    nums = [0,1,2,3,4,5,6,7,8,9]
    for i in range(randint(4,7)):
        outList.append(nums[randint(0,9)])
        todo -= 1

def addLowerCase():
    global todo, outList
    lowerCase = list(ascii_lowercase)
    for i in range(todo):
        outList.append(lowerCase[randint(0,25)])
        todo -= 1

def createPasswd(times):
    global outList, todo
    passwdList = []
    for i in range(times):
        outList = []
        todo = 24
        addScpecialChars()
        addUpperCase()
        addNumbers()

        shuffle(outList)

        todo -= 4
        addLowerCase()

        for i in range(randint(1,9)):
            shuffle(outList)

        todo = 3
        addLowerCase()

        for i in range(3):
            outList[i],outList[len(outList)-(i+1)] = outList[len(outList)-(i+1)], outList[i]

        todo = 1
        addLowerCase()

        passwdList.append(outList)

    return passwdList

def main():
    amount = intConvert(input('hoeveel wachtwoorden wilt u?\n'))
    if isinstance(amount,int) and amount > 0:
        mainList = createPasswd(amount)
        s = '' if amount < 2 else 's'
        print(f'generated password{s}:')
        for i in range(amount):
            print(*mainList[i],sep='')
    else:
        print('invalid input')
        main()

main()