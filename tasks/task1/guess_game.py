import os
import random
import time

for i in range(random.randint(1, 10)):
    guess_num = random.randint(1, 10)
    try:
        text = input('Guess the num ')
        opinion_num = int(text)
    except ValueError:
        print(f'Problems with type of variable {text}')
    else:
        if guess_num == opinion_num:
            print('You win ')
            break
        else:
            print('write again ')
            time.sleep(5)
            os.system('cls||clear')
