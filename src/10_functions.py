# Write a function is_even that will return true if the passed-in number is even.
# YOUR CODE HERE
def is_even(n):
    if int(n) % 2 == 0:
        print(True)
    else:
        print(False)

is_even(2)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE
def is_even_v2(n):
    if int(n) % 2 == 0:
        print('Even!')
    else:
        print('Odd')

is_even_v2(num)

# # Read a string from the keyboard
s = input("Enter some characters: ")

# # Write a function that reverses the input string s
# # YOUR CODE HERE
def reverse_string(s):
    print(''.join(reversed(s)))

reverse_string(s)


### Python 2 lect. notes 

# Why are return statements important?
# without a return statement, nothing 'comes out' of the function

# passing by reference vs. passing by value
# PBR: referencing a list, etc. Pass that reference in to function; the function changes the data, and those changes to the data persist, even when exiting the function

# PBV: the function receives a brand new copy of the data; outside the function,
# the changes the function made to the data do not persist, unless we explicitly save the data

