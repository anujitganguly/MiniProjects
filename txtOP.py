# main code
p = input("Enter a value: ")
print(p)

# Command to open a txt file. If file is not present, it will create and open the same
m = open('trial.txt', 'a')
# Write output in a new line inside txt file
m.write(p +'\n')
# Save and close txt file
m.close()