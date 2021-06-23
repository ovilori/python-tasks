#code to implement a number guessing game
#generates a random number between 1 and 10 and allow the user to guess
#prompts the users for their guess until they guess correctly
#finally displays the number of guesses
#displays the current guess number.
#if the guess is too low, tells the user "Your guess is too low, try again!"
#if the guess is too high, tells the user "Your guess is too high, try again!"
#if the user enters a nonnumeric value, tells the user "Numbers only, please!"

#code to implement a number guessing game
#generates a random number between 1 and 10 and allow the user to guess
#prompts the users for their guess until they guess correctly
#finally displays the number of guesses
#displays the current guess number.
#if the guess is too low, tells the user "Your guess is too low, try again!"
#if the guess is too high, tells the user "Your guess is too high, try again!"
#if the user enters a nonnumeric value, tells the user "Numbers only, please!"

print('Game time! Guess a number between 1 and 10')

import random as alias

number = alias.randint(1,10)
user_input = 0
count = 0

while user_input != number:
    count += 1
    user_input = input(f'Enter guess #{count}: ')
    
    if user_input.isnumeric() == False:
        print('Numbers only, please!')
        continue

    elif int (user_input) < number:
        print('Your guess is too low, try again!')

    elif int (user_input) > number:
        print('Your guess is too high, try again!')
        
else:
    print(f'You guessed it in {count} tries!')

#alternative code below:

""" print('Game time! Guess a number between 1 and 10')

import random as alias

number = alias.randint(1,10)
user_input = 0
count = 0

while user_input != number:
    count += 1
    user_input = input(f'Enter guess #{count}: ')

    if user_input.isnumeric():
        user_input = int(user_input)
    else:
        print('Numbers only, please!')
        continue

    if user_input < number:
        print('Your guess is too low, try again!')
    elif user_input > number:
        print('Your guess is too high, try again!')

else:
    print(f'You guessed it in {count} tries!') """

