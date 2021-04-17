import time

characters = 'abcdefghijklmnopqrstuvwxyz'
capCharacters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '`~!@#$%^&*()-_=+[]{};:\\\'\",.<>?/'


def takeNumberOfCharactersList():
    try:
        numberOfCharactersList = input('number Of Character\'s List: ')
        numberOfCharactersList = int(numberOfCharactersList)
        return numberOfCharactersList
    except Exception:
        print('there is an error.')
        print('please type a correct number.')
        exit()


def takeAllChar():
    print('do you want default, select or costume characters')
    print("1) default\n2) select\n3) costume\n\n99) exit")
    charType = input("your choice: ")
    if charType == '1':
        allChar = characters + capCharacters + numbers + symbols
        return allChar
    elif charType == '2':
        print('select the list you want')
        print('1) characters\n2) capCharacters\n3) numbers\n4) symbols\n5) done\n\n99) exit')
        selectedChar = ''
        while True:
            selectMode = input('your choice: ')
            if selectMode == '1':
                selectedChar += characters
            elif selectMode == '2':
                selectedChar += capCharacters
            elif selectMode == '3':
                selectedChar += numbers
            elif selectMode == '4':
                selectedChar += symbols
            elif selectMode == '5':
                break
            elif selectMode == '99':
                exit()
            else:
                print('this isn\'t from the list')
                exit()
        print(selectedChar)
        return selectedChar
    elif charType == '3':
        costumeChar = input('type your characters: ')
        if costumeChar == '':
            print('list is empty')
            exit()
        else:
            return costumeChar
    elif charType == '99':
        exit()
    else:
        print('this isn\'t from the list')
        exit()


def generateList(selectedChar, selectedNumberOfCharactersList):
    import itertools
    wordListFile = open('wordlist.txt', 'a')
    for xs in itertools.product(selectedChar, repeat=selectedNumberOfCharactersList):
        char = ''.join(xs)
        print(char)
        wordListFile.write(str(char + '\n'))
    wordListFile.close()


if __name__ == '__main__':
    startTime = time.time()
    generateList(takeAllChar(), takeNumberOfCharactersList())
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
