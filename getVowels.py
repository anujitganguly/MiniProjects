# Funtion to find vowels
def get_vowels(String):
    return [each for each in String if each in "aeiouAEIOU"]
# Enter user input
word = input("Enter a word to check vowels: ")
# Calling the function
get_vowels(word)

# Printing output
print("The vowels in the above word are: ",get_vowels(word))