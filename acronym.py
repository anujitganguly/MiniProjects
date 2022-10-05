# Take user input
user_input = str(input("Enter a phase: "))

# split() is used to take multiple words
text = user_input.split()

# split() will work after a single space
acr = " "

# Loop
for i in text:
    acr = acr + str(i[0]).upper()

# Print acronym
print(acr)