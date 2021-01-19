import random

value = random.randint(1, 10)
count = 0
guess = 0
print('Guess a number between 1 and 10')
while guess != value:
    count+=1
    print(f'Enter guess #{count}:')
    guess=input()
    if  guess.isnumeric:
        guess=int(guess)
    else:
        print("please enter valid number")
        
    if int(guess)<value:
        print(" Your guess is  low, try again!")
    elif int(guess)>value:
        print(" Your guess is  high, try again!")
else:
    print(f'You guessed it in {count} tries!')