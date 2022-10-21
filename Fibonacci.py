nterms = int(input("Enter number of terms: "))
# Set 1st & 2nd value by default and count
n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("Please Enter a positive value: ")
elif nterms == 1:
    print("Fibonacci sequence upto ",nterms," : ")
    print(n1)
else:
    print("Fibonacci sequence upto ", nterms, "terms: ")
    while count < nterms:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1