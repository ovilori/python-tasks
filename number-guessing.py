#code to implement a number guessing game
#generates a random number between 1 and 5 and allow the user to guess
#prompts the users for their guess until they guess correctly
#finally displays the number of guesses

import random

print('Let\'s play a number guessing game')

number = random.randint(1, 5)
user_input = 0
count = 0

while user_input != number:
    count += 1
    user_input = input('Guess a number between 1 and 5: ')

#continues counting all user input as a guess even if it is not a numerice value
    if user_input.isnumeric() == False:
        continue 

else:
    print (f'You guessed it in {count} tries!')
