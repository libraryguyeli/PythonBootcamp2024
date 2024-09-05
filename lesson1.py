# Function chaining to strip whitespace from beginning and end of input, and convert to all uppercase
name = input("What's your name?").strip().upper()
# This is also a viable method for producing the same results as above without function chaining.
name = name.strip()
name = name.upper()
# Concatenating three strings together: hello, the name variable, and a period.
print("Hello, " + name + ".")
# F-string/formatted string: same result as above, but with less need for attention to detail.
print(f"Hello, {name}.")



# Creating our own function, with a default value if the name parameter is not provided.
def greet(name = "world"):
    # This name variable lives inside the greet function and cannot be used outside of it.
    print(f"Hello, {name}.")

# The greet function receives a name when we call it and pass an argument to it in the form of a string inside the parentheses.
greet("Eli")
greet("John")
greet("Fernando")
# If we do not pass an argument to the function, we programmed defensively and built in a default value, which would be "world".
# If we had not coded a default value, the following line would render an error in our program.
greet()

# We do not have to pass only strings to our greet function. We can pass variables that store strings as data.
username = input("Enter your username: ")
greet(username)



# Creating another function that takes more than one parameter, separated by a comma.
def add(a, b):
    # a and b live locally in this function. We cannot print(a) outside of this function and get the result we expect.
    print(a + b)

# Function nesting, where we converted the user input to an integer (whole number) in the same line that we ask for input and assign a value to the variable.
num1 = int(input("number 1: "))
num2 = int(input("number 2: "))
# The next four lines produce the same result as the previous two, but without function nesting, which may be easier to understand getting started.
num1 = input("number 1: ")
num2 = input("number 2: ")
num1 = int(num1)
num2 = int(num2)
# Calling our function with the two user-inputted numbers
add(num1, num2)