import os
import random

for i in range(random.randint(1, 10)):
    guess_num = random.randint(1, 10)
    opinion_num = int(input('Guess the num '))
    if opinion_num == guess_num:
        print('You win ')
        break
    else:
        print('write again ')
        os.system('cls||clear')
