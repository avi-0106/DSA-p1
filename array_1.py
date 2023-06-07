# Create an array
array1 = [1, 2, 3, 4, 5]
# Modify an element at index 2
array1[2] = 'GG'
# Append a new element to the end of the array
array1.append('Hi')

# Print all elements in the array
for arr in array1:
    print(arr)
print("\n")

# Iterate over the array with both index and value
for ind, val in enumerate(array1):
    print("Index: ", ind)
    print("Value: ", val)
print("\n")

# Print the entire array
print(array1)
# Remove an element from the array by value
array1.remove('Hi')
print(array1)
# Remove an element from the array by index
array1.pop(4)
print(array1)
print("\n")

# Access an element at index 3
print(array1[3])
# Get the length of the array
print(len(array1))
# Get the type of the array
print(type(array1))