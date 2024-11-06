"""
Assignment 4: Wednesday, October 2nd
"""

# I wanted user input for all my dicts, so I created a function that I could call 3 times instead of asking for 4 variables 3 times.
def person_input():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    city = input("City: ")
    return (first_name, last_name, age, city) # Returned a tuple, which is an immutable (unchangeable) data structure. Lists are similar but mutable (changeable).

# Since I was also going to be making 3 dicts, I made this a function to avoid repetition in my code.
# Since tuples are immutable, I knew that the order would always be preserved, which means I could index them like this.
def person_dict(person):
    dictionary = {
        "first_name": person[0],
        "last_name": person[1],
        "age": person[2],
        "city": person[3]
    }
    return dictionary

# Printed dicts are a little unsightly! So I made a function to print all my person variables in a more readable fashion.
def print_person(person):
    print(f"{person["first_name"]} {person["last_name"]} ({person["age"]}) from {person["city"]}")

person1 = person_input()
person1 = person_dict(person1)
print(person1) # To show how it looks printing a dict straight up
print_person(person1)

person2 = person_input()
person2 = person_dict(person2)

person3 = person_input()
person3 = person_dict(person3)

people = [person1, person2, person3]
for person in people:
    print_person(person)