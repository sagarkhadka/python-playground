import random

gNum = int(input('Enter the guess limit: '))
guess = random.randint(1, gNum)

# print(guess)

print(f'I have guessed the number \nnow you try guessing the number.')
num = int(input('Enter your guess: '))

if (num == guess):
    print(f'Correct you guessed correct.')
else:
    if num < guess:
        print("Too Low ! Try guessing higher number.")
    else:
        print("Too High! Try guessing lower number")
