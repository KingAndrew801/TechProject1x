import random
from random import randrange

down = 'y'
randnum = None
score = 0
def startgame():
    score = 0
    highscore = 100
    guess = None
    down = 'y'
    print('-' * 50)
    print('''Welcome to the guessing game!
    Just type a number and try to guess the number!''')
    print('-' * 50)
    gamerunning = True
    gaming = True
    while down == 'y':
        while gamerunning == True:
            randnum = randrange(1, 11)
            while gaming == True:
                try:
                    guess = int(input("What's your guess?"))
                except ValueError:
                    print('guess with numbers dude')

                if guess > randnum:
                    print("Go lower")
                    score += 1
                if guess < randnum:
                    print('Go higher.')
                    score += 1
                if guess == randnum:
                    print('you got it!')
                    print(f'Game is over bro, you score is {score}')
                    if score < highscore:
                        highscore = score
                        print('You got high score!')
                        score = 0
                        try:
                            decide = input("Do you want to play again?")
                            if decide != 'y' or 'n':
                                raise Exception('Thats not a valid choice, homie!')
                            else:
                                if decide == 'n':
                                    down = decide
                                    gamerunning = False
                                    gaming = False
                                if decide == 'y':
                                    gamerunning = True
                                    gaming = False
                                    continue
                        except:
                                    continue


startgame()