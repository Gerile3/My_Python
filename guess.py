# Basic guess the number game
import random
print('Guessing Game')

# Build the number and get user's guess
number = random.randint(0, 9)
user = int(input('enter a number:'))
guess_track = int()

# Compare the user number with the number program have picked
while user != -1:

    if user != number and user < number:
        print('You guessed low')
        user = int(input('enter a number:'))
        guess_track = guess_track+1
    if user != number and user > number:
        print('You guessed high')
        user = int(input('enter a number:'))
        guess_track = guess_track+1
    if user == number:
        print('You guessed right!')
        print('enter a number to play and type -1 to quit:')
        guess_track = guess_track+1
        user = int(input())

# Print the result        
print('your total guesses:', guess_track)
