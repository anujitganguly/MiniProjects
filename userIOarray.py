# Array declaration and user input for array length
a = []
n = int(input("Enter lenght of array: "))

# Append array elements inside array
for i in range(0, n):
    l = int(input())
    a.append(l)

# Print the array elements
print(f"The {n} elements in array are:-\n")
print(a)

# Append additional element in existing array
m = int(input("Enter additional element to append in array: "))
a.append(m)
print(f"The new array is:-\n")
print(a)

# Reverse the array
a.reverse()
print("The reverse array is:-\n")
print(a)