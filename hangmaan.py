import random
import os


def main():
    words = readData()
    play(words)


def readData():
    try:
        words = []
        with open('assets\data.txt', 'r') as f:
            words = [i.replace('\n', '') for i in f]
        return words
    except FileNotFoundError as e:
        print('Error File not found', e)


def play(words):
    title = ("""
 ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ 
                                                                       """)
    try:
        word = random.choice(words)
        w = list(word)
        l = list('_'*len(word))
        lifes = 5
        print(word)

        while l != w:
            a = False
            os.system('clear')
            print(title)
            print(' '.join(l).upper())

            letter = input('\n\nTries left: ' + str(lifes) +
                           '\nGuess a letter in lower case: ')
            assert len(letter) == 1, 'Press ONLY 1 letter'

            for i in range(len(w)):
                if w[i] == letter:
                    l[i] = w[i]
                    a = True
            if not a:
                lifes -= 1
                if lifes == 0:
                    os.system('clear')
                    print(title)
                    print('\n\nGame over... :(')
                    print('The word was ' + ''.join(w).upper())
                    break

        if(l == w):
            os.system('clear')
            print(title)
            print('GANASTE!!\nLa palabra era ' + ''.join(w).upper())

    except:
        print('Ended abruptly...')


if __name__ == '__main__':
    main()
