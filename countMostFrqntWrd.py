words = []
file = input("Enter filename with extension: ")
ct = int(input("Enter upto what count you want to display result: "))
with open(file, "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
top = counts.most_common(ct)
print(top)