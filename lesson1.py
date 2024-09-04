# name = input("What's your name?").strip().upper()
# name = name.strip()
# name = name.upper()
# print("Hello, " + name + ".")
# print(f"Hello, {name}.")

def greet(name = "world"):
    print(f"Hello, {name}.")

greet("Eli")
greet("John")
greet("Fernando")
greet()

# username = input("Enter your username: ")
# greet(username)

def add(a, b):
    print(a + b)

num1 = int(input("number 1: "))
num2 = int(input("number 2: "))
# num1 = input("number 1: ")
# num2 = input("number 2: ")
# num1 = int(num1)
# num2 = int(num2)
add(num1, num2)