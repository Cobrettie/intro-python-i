### Lists ### 

# Create a list #
# Access list items #
# Change the value of a list item # 
# Loop through a list # 
# Check if a list item exists # 
# Get the length of a list # 
# Add an item to the end of a list # 
# Add an item at a specified index #
# Remove an item #
# Remove an item at a specified index #
# Empty a list 
# Use the list() constructor to make a list

# Create a list
my_list = [1, 2, 3, 4, 5]

# Access, change value of list item
my_list[1] = 222

# Loop through  a list
for i in my_list:
    print(i)

# Check if item exists 
if (4 in my_list):
    print('Item exists!')

# Get length of list #### ASK IF THIS IS THE PROPER WAY TO DO THIS
print('My list has', len(my_list), 'items at this point in python file')

# Add item to end of list
my_list.append('new last item')

# Add item at specific index, remember 0 based indexing
my_list.insert(3, 444)

# Remove item
my_list.remove(5)
print(my_list)

# Remove item at specified index
my_list.pop(1)

# Empty a list
my_list.clear()

# use the list() constructor to make a list
constructor_list = list(('one', 'two', 'three', 'four', 'five'))