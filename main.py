import random 
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([1,-1,0]) # computer's choice
print("Welcome to Snake, Water, Gun game!") 

youstr = input("Enter your choice: ") # s for snake, w for water, g for gun
youDict = {"s": 1, "w": -1, "g": 0} # for user input
reverseDict = {1: "snake", -1: "water", 0: "gun"}  # for displaying choices 

if youstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}") 
## Now we will compare the choices of computer and user to determine the winner
# The rules are:
if(computer == you):
    print("It's a tie!")

else:
    if (computer == -1 and you == 1):
        print("you win!")
    
    elif(computer == -1 and you == 0):
        print("You lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer == 1 and you == 0):
        print("You win!")

    elif(computer == 0 and you == -1):
        print("You win")

    elif(computer == 0 and you == 1): 
        print("You lose!")

    else:
        print("Something wrong")
# The game logic is complete and handles all cases correctly.
