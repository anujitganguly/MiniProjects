# Default value of SUM
sum = 0

# Check condition
while (True):
    num = input("Enter price of Item or 'q' to exit: \n")
    # Keep adding bill
    if (num != 'q'):
        sum = sum + int(num)
        print(f"Order value so far: {sum}")

   # If user wants to quit
    else:
        print(f"Your bill is {sum}. \nTHANKS FOR SHOPPING WITH US")
        break