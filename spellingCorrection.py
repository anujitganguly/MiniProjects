# Import required library
from textblob import TextBlob

# Input function
def Convert(string):
    li = list(string.split())
    return li

# Using user input
str1 = input("Enter your word: ")
words = Convert(str1)
corrected_words = []

for i in words:
    corrected_words.append(TextBlob(i))

print("Wrong Word: ", words)
print("Possible correct word: ",)
for i in corrected_words:
    print(i.correct(), end=" ")