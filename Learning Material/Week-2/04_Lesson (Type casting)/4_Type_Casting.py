# Type casting
# int() --> to convert any data type to integer but not string alphabets
# float() --> to convert any data type to float but not string alphabets
# str() --> to convert any data type to string
# bool() --> to convert any data type to boolean value
# list() --> to convert any data type to list
# tuple() --> to convert any data type to tuple
# set() --> to convert any data type to set
# dict() --> to convert any data type to dictionary

n =  20
print('The type of n:', type(n))
f = float(n)
print('The type of f:', type(f))
h = 24
string = str(h)
print('The type of string:', type(string))

# In case of any non-zero value (it gives True)
b = bool(n)
print('The type of b:', type(b))