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
                if guess > 10 or guess < 1:
                    print(f"That guess is out of range my dude. Choose between 1 and 10.")
                if guess == randnum:
                    print('you got it!')
                    print(f'Game is over bro, you score is {score}')
                    gamerunning = False
                    if score < highscore:
                        highscore = score
                        print('You got high score!')
                        score = 1
                        gamerunning = False
            except ValueError:
                print('guess with numbers dude')

        deciding = True
        while deciding == True:
            try:
                down = input("Do you want to play again?  ")
                if down != 'y' and down != 'n':
                    raise Exception('Thats not a valid choice, homie!')
                if down == 'n':
                    print(f'Fine, game is over, your highscore is {highscore}')
                    deciding = False
                    break
                if down == 'y':
                    print(f"LET'S GET IT! High score so far is {highscore}.")
                    gamerunning = True
                    deciding = False
                    break
            except Exception as e:
                print(e)




startgame()