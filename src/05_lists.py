# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print(x.append(4))

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(x.extend(y))

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print(x.remove(8))

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
print(x.insert(5, 99))

# Print the length of list x
# YOUR CODE HERE
print("length of x: ", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for n in x:
    print("n * 1000: ", n * 1000)

z = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
    [40 ,41, 42, 43, 44, 45, 46, 47, 48, 49],
    [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
    [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
    [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
    [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
    [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
]

# Print the first element from each nested list in the matrix z
# YOUR CODE HERE
for n in z:
    print("First el from each nested list: ", n[0])

# Print all of the elements that lie on the left-to-right 
# diagonal of matrix z 
# YOUR CODE HERE


# what if we also want the index of the element?
# enumerate gives us access to each list element and its index
for index, elem in enumerate(y):
    print(f"element {index} is {elem}")


# how to loop certain number of times
# range() 'start, stop, increment by'