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


'''
Some extra notes:

1. Contiguous Memory: Arrays store elements in contiguous memory locations, 
allowing for efficient access to elements using their indices. This property 
makes arrays suitable for random access and enables constant-time retrieval 
of elements.

2. Fixed Size: Arrays have a fixed size determined during initialization, 
which remains constant throughout the lifetime of the array. This makes arrays 
suitable for scenarios where the size is known and doesn't change frequently.

3. Index-based Access: Elements in an array are accessed using their indices. 
The index represents the position of an element within the array, starting from 
0 for the first element. This allows for efficient retrieval and manipulation 
of elements by their position.

4. Efficient Search: Arrays facilitate efficient search operations when the index 
of an element is known. Accessing an element by index has a time complexity of O(1) 
since it involves a direct memory access.

5. Memory Efficiency: Arrays have a low memory overhead as they store only the 
elements themselves and don't require additional pointers or metadata. This makes 
arrays memory-efficient compared to some other data structures.

6.Sequential Storage: Elements in an array are stored sequentially in memory, 
which makes them ideal for scenarios that involve sequential access, such as 
iterating over the elements.

7. Limited Insertion/Deletion: Insertion and deletion of elements in an array 
can be inefficient when performed frequently or at arbitrary positions. Inserting 
or deleting an element at the beginning or middle of an array requires shifting 
elements, resulting in a time complexity of O(n), where n is the number of elements.

8. Static Structure: Arrays have a static structure, meaning their size cannot be 
easily changed once allocated. To overcome this limitation, dynamic arrays or 
resizable arrays are often used, which allow for resizing and efficient insertion/deletion 
at the end.

9. Versatile Applications: Arrays have a wide range of applications in various domains, 
including algorithms, data storage, numerical computing, image processing, and more. 
They provide a foundation for many other data structures and algorithms.

10. Multidimensional Arrays: Arrays can be extended to multiple dimensions, 
allowing for the representation of matrices, tables, or higher-dimensional 
data structures. Multidimensional arrays provide efficient access to elements 
using multiple indices.

'''