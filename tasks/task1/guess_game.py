import os
import random

for i in range(random.randint(1, 10)):
    guess_num = random.randint(1, 10)
    opinion_num = 0
    try:
        opinion_num = int(input('Guess the num '))
    except ValueError:
        print(f'Problems with type of variable {opinion_num}')
    if opinion_num == guess_num:
        print('You win ')
        break
    else:
        print('write again ')
        os.system('cls||clear')
