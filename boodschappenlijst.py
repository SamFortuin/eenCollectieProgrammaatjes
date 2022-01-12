from string import ascii_lowercase,capwords
from time import sleep

a = {} #blank dict for later

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

def main():
    addEntry = input('Wat wilt u toevoegen en hoeveel? (artikel, hoeveel)\n').lower().split(',')
    amount = intConvert(addEntry[1])
    if isinstance(amount,int) and amount > 0:
        a.update({addEntry[0]:amount})
        again = input('Wilt u meer toevoegen aan de lijst?\n').lower()[:1]
        if again == 'y' or again == 'j':
            main()
        else:
            for x,y in a.items():
                print(f'{y:>2}x {capwords(x)}')
    elif type(amount) != int:
        print('geen nummer, probeer opnieuw')
        main()
    elif amount < 1:
        print('negatief nummer, probeer opnieuw')
        main()

main()
