st_year = int(input("Enter 1st year investment: "))
f_value = int(input("Enter the amount you are promised to get: "))
years = int(input("Enter total years of investment: "))

div = f_value/st_year
by_t = 1/years
m = div**by_t
yi = (m-1)*100
print("CAGR is: %.2f" %yi)