import random 
# Number Guessing Game
# The computer will generate a random number between 1 and 100
n = random.randint(1,100)
a = -1
guesses = 0
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")    
print("Try to guess it in as few attempts as possible!")
# The user will input their guess
print("Enter your guess below:")

while ( a != n):
    a = int(input("Guess the Number: "))
    if(a > n):
        print("Lower number Please")
        guesses += 1

    elif(a < n):
        print("Higher Number Please")
        guesses += 1

# If the user guesses the number correctly
print(f"You have guessed the number {n} in {guesses} attempts!")
print("Congratulations! You win!")
print("Thank you for playing the Number Guessing Game!")
print("Goodbye!")
# End of the game
# The game ends when the user guesses the correct number

