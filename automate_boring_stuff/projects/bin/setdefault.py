### Following the Fantasy Inventory exercise, some practice using setdefault()
### from https://www.learnbyexample.org/python-dictionary-setdefault-method/

'''
Syntax is: dictionary.setdefault(key, default)
Where the 'key' is required, and the 'default' is optional.

The 'default' is the value to insert is the key does not already exist in the dict. Default value is None.
'''


# Insert a key 'job' with defaul value 'Dev'
D = {'name': 'Bob', 'age': 25}
v = D.setdefault('job','Dev')

print("Here is the variable D: ", D)
print("Here is the variable v: ", v) # Prints just the default



## Different cases for using sefdefault()
# 1. To see if a key is present. If so, it will return the value for that key
D = {'name': 'Jack', 'age': 25}
v = D.setdefault('name') # This will always return the value of the key, REGARDLESS of what you pass as 'default'

print(v) 

# With default specified
z = D.setdefault('name', 'Max') 
print(z) # Prints Jack - because this method will not override values in existing keys



# 2. To see if a key is NOT in the dictionary, with the default specified
print("See the very first example.")

# 3. To see if a key is NOT in the dict, with NO default specified
D = {'name': 'Bob', 'age': 25}
v = D.setdefault('job')

print(D)
print(v)