import random

cowbull = [0,0] # Initialised list to keep track of score
counter = 0 # Initialised counter to keep track of the number that was guessed

def compare_numbers(number, user_guess): # Added code to handle the user's guesses
    global counter
    for i in range(len(number)):
        if user_guess == number[i] and counter == i:
            cowbull[1] += 1
            counter += 1
            return cowbull
        elif user_guess == number[i] and counter != i:
            if user_guess == number[counter]:
                cowbull[1] += 1
                counter += 1
                return cowbull
            cowbull[0] += 1
            return cowbull
    print("Your guess isn't quite right, try again.") # Moved the print statement here
    return cowbull

playing = True #gotta play the game
number = str(random.randint(1000,9999)) # Now this line actually gives a 4 digit number rather than 0-9999
guesses = 0
print(number) # Fixed print statement

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") # Changed raw_input to input
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + " guesses! The number was "+str(number)) # Changed print with proper grammar #redundant exit
# Moved else print statement up into function
