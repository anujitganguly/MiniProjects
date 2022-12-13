p = float(input("Enter monthly SIP value: "))
r = float(input("Enter interest rate: "))
n = float(input("Enter total number of months you need to invest: "))
x = float(p*n)

# actual formula to find final value
i = float(r/1200)
m = (1+i)**(n-1)
z = p*m*(1+i)
f1 = z/i
# command to take upto 2 decimal values before running the INR function
f1 = f'{f1:.2f}'

# function to change normal output to INR terms
def formatINR(amount):
    s1, *d1 = str(amount).partition(".")
    r1 = ",".join([s1[x1-2:x1] for x1 in range(-3, -len(s1), -2)][:: -1]+[s1[-3:]])
    return "".join([r1]+d1)

# variables for storage
v5 = formatINR(f1)
v6 = formatINR(x)


print("\nFinal amount will be: INR", v5)
print("Your total investment: INR", v6)


