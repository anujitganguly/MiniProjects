# Import necessary module
from countryinfo import CountryInfo

# Input country name
val = input("Enter the country name: ")
# Fetching country info
country = CountryInfo(val)

# Printing the values
print("Capital is: ", country.capital())
print("Currency is: ", country.currencies())
print("Language is: ", country.languages())
print("Neighbouring Countries are: \n", country.borders())
print("Also known by following names: \n", country.alt_spellings())

### This code can be merged with currency converter code to provide better output by checking currency from here and converting it there ###