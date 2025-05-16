#==============================================================================================================
# While Loops
#==============================================================================================================


# While loops execute a set of statements as long as a condition is true.

# While loop example
count = 0
while count < 5:
    print(f"Count is {count}.")
    count += 1  # Same as count = count + 1


# While Loop - Guessing Game
''' Important to understand here: Initialization: Line 12 initializes the guess variable with a value that's guaranteed not to be the secret number. This ensures that the condition for entering the while loop (guess != secret_number) is true at the start.
    If we don't initialize guess before the loop, Python would raise an error when it reaches the condition in the while loop because it wouldn't know what guess refers to.
    
    Logic Flow: The value -1 is chosen because it's outside the range of possible correct answers. This choice is arbitrary, and any value outside the expected range of correct answers would work.
    The key is to start with a value that ensures the loop runs at least once and keeps running until the user guesses correctly. '''

secret_number = 3
guess = -1

while guess != secret_number:
    guess = int(input("Guess a number between number 1 and 10: "))
    if guess == secret_number:
        print("You guessed it!")
    else:
        print("Sorry, guess again.")

print("Game Over.")
