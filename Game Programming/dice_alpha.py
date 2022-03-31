# A simple program a game between user and computer
import random
import time

# Create a main function under which the program executes
def dice():
    player = random.randint(1,6)               
    print('You called ',player)   

    ai = random.randint(1,6)                   
    print('The computer rolls...')
    time.sleep(2)
    print('The computer has rolled a ',ai)

    if player > ai:
        print('You win!')
    elif player == ai:
        print('Tie game!')
    else:
        print('You lose!')

    print('Quit? Y/N')
    cont_inue = input()

    if cont_inue == "Y" or cont_inue == "y":
        exit()
    elif cont_inue == "N" or cont_inue == "n":
        pass
    else:
        print('I did not understand that, playing again')

while True:
    print('Press return to roll your dice')
    roll = input()
    dice()