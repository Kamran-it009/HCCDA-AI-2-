# 1.  Function definition
def hello():
    print('hello world')

hello() # Function calling


# 2. Function with parameter
def hello2(name):
    print(f'hello {name}')

hello2('Kamran') # Function calling


# 3. Function with parameter and return value
def hello3(name):
    return f'hello {name}'

res = hello3('Kamran') # Function calling.
print(res)

# ---------------------------------------------------------
# Case no: 1
def sum1(a, b): # a and b are parameters.
    c = a + b
    return c # returned value

# function calling
x = sum1(10, 15) # 10 and 15 are arguments.
print(x)


# Case no: 2
def sum2(a = 20, b = 15): # Default parameters.
    x = a + b
    return x # returned value

answer  = sum2()
print(answer)

# Case no: 3
answer = sum1(a = 5, b = 26) # Keyword Arguments
print(answer)

# 4. Lamda function
add = lambda x, y : x + y

result = add(2, 3)
print(result)

# 5. Function with unlimited auguments
def sum(*a):
    sum = 0  # 10, 89, 10, 89, 78, 14, 15
    for i in a:
        sum = i + sum
    
    return sum

sum(10, 89, 10, 89, 78, 14, 15)


# 6. Function with unlimited keyword auguments
def sum(**a):
    print(a)

sum(a = 5, b = 5, c = 6, d = 10, e = 67)

# 7. Recursive functions
def name(a):
    print('----------------')
    print(a)
    name(a)

name('Kamran')


# Map Functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)

print(list(squared_numbers))

# Nested Funtions
def outer_function():
    print('Calling the outer')
    def inner_function():
        print("This is the inner function.")
    inner_function()  # Calling the inner function inside the outer function

outer_function()