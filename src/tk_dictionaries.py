### Dictionaries ### 

# Create a dictionary # 
# Access the items of a dictionary # 
# Change the value of a specific item in a dictionary # 
# Print all key names in a dictionary, one by one #
# Print all values in a dictionary, one by one # 
# Use the values() function to return values of a dictionary #
# Loop through both keys and values, by using the items() function # 
# Check if a key exists # 
# Get the length of a dictionary # 
# Add an item to a dictionary # 
# Remove an item from a dictionary #
# Empty a dictionary # 
# Use the dict() constructor to create a dictionary #


# Create a dictionary
my_dict = {
    'username': 'Cobra',
    'dob': '1/7/4',
    'online': True,
    'journey': 'in progress'
}

# Access the items of a dictionary 
print(my_dict['username'])

# Change the value of a specific item in a dictionary
my_dict['dob'] = '12/27/84'

# Print all key names in a dictionary, one by one
for key in my_dict:
    print('key: ', key)

# Print all values in a dictionary, one by one
for value in my_dict:
    print('value: ', my_dict[value])

# Use the values() function to return values of a dictionary
all_values = my_dict.values()
print('my_dict as list', all_values)

# Loop through both keys and values, by using the items() function
all_keys_values = my_dict.items()
print('all keys/values as tuple', all_keys_values)

# Check if a key exists
key_to_lookup = 'username'
if key_to_lookup in my_dict:
    print(key_to_lookup, 'key exists!')
else:
    print('key does not exist!')

# Get the length of a dictionary
print('Length of my_dict is', len(my_dict), 'key/value pairs')

# Add an item to a dictionary
my_dict['providing'] = 'value'

# Remove an item from a dictionary
my_dict.pop('username', 'Could not locate username key')

# Empty a dictionary
# my_dict.clear()

# Use the dict() constructor to create a dictionary
new_dict = dict(username = 'Cobra', age = 297, favorite_color = 'blue')
