# Importing in-biult library
from forex_python.converter import CurrencyRates

# Calling function
c = CurrencyRates()

# User Inputs
from_curr = input("Enter the Currency you are converting from: ").upper()
amount = int(input("Enter the amount: "))
to_curr = input("Enter the currency you are converting to: ").upper()

# Actual calculations
result = c.convert(from_curr, to_curr, amount)

# Output
print(from_curr, " to ", to_curr, " of ", amount, " is: ", result)