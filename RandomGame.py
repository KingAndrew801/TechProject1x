import random
from random import randrange


def startgame():
    score = 1
    highscore = 100
    guess = None
    down = 'y'
    print('-' * 50)
    print('''Welcome to the guessing game!
    Just type a number and try to guess the number!''')
    print('-' * 50)

    while down == 'y':
        randnum = randrange(1, 11)
        gamerunning = True
        while gamerunning == True:
            try:
                guess = int(input("What's your guess?   "))
                if guess > randnum:
                    print("Go lower")
                    score += 1
                if guess < randnum:
                    print('Go higher.')
                    score += 1
                if guess == randnum:
                    print('you got it!')
                    print(f'Game is over bro, you score is {score}')
                    gamerunning = False
                    if score < highscore:
                        highscore = score
                        print('You got high score!')
                        score = 1
                        down = None
            except ValueError:
                print('guess with numbers dude')
        try:
            down = input("Do you want to play again?  ")
            if down != 'y' or 'n':
                raise Exception('Thats not a valid choice, homie!')
            if down == 'n':
                print(f'Fine, game is over, your highscore is {highscore}')
                gamerunning = False
                break
            if down == 'y':
                gamerunning = False
                break
        except Exception as e:
            print(e)




startgame()