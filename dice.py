# Importing random module
import random

# Set maximum and minimum limit of dice
max_val = 6
min_val = 1

# Command to loop the rolling through user input
roll_again = 'yes'

# Loop
while roll_again == "yes" or roll_again == "y":
    print("The values are: ")

# Generating and showing 1st random value
    print(random.randint(min_val, max_val))

# Generating and showing 2nd random value
    print(random.randint(min_val, max_val))

# Ask user if they want to re-roll. Anything other than "yes" or "y" will close the code
    roll_again = input("Press Y to roll again, anything else to exit:  ")