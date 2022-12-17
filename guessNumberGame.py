import random
n = random.randrange(1, 10)
guess = int(input("Enter number between 1 to 10: "))
while n != guess:
    if guess < n:
        print("Too low, try again!")
        guess = int(input("Enter the number again: "))
    elif guess > n:
        print("Too high, try again!")
        guess = int(input("Enter the number again: "))
    else:
        break
print("You guessed it right!!")