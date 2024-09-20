import random
# Create your own list with at least 4 items (Strings)

bookbag = ["Book", "Pen", "Phone", "Water"]

# print(bookbag)
'''
# For is the keyword, thing is a temporary variable, in is a keyword, bookbag is the name of the list
for thing in bookbag:
    print(thing)
    print(thing + " in my bag")
print("Loop complete")
print(thing)

# Example of a For Loop looping through each character of a string
birthday = input("What is your birthday?")

for letter in birthday:
    if letter == "J":
        print("Your birthday month has J in it.")


counter = 0
while counter < 10:
    print("I am awesome")
    counter = counter + 1
    print(counter)


# Secret Number Game
guess_counter = 0
secret_num = random.randint(1,50)

while guess_counter < 10:
    guess_counter = guess_counter + 1
    player_guess = int(input("What is the secret number?"))
    if player_guess == secret_num:
        print(f"You win!! It took you {guess_counter} guesses.")
        break

    elif player_guess < secret_num:
            
        print("Try a higher number. Guess again")
    else:
        print("Try a lower number. Guess again.")



# Index and slicing strings
backpack = ["Book","Radio","Phone", "Water"]

## Prints first element in the list
print(backpack[0])
## Prints first two elements in the list
print(backpack[0:2])
print(backpack[:2])
## Prints last element
print(backpack[-1])

phrase = "I am awesome... but only on Tuesdays."

print(phrase[5:])
print(phrase[:15])

    
open = False
password = "butterscotch"
counter = 0

while open != True and counter < 3:
    counter += 1
    guess = input("What is the password?")
    if guess == password:
        open = True
        print("Unlocked!")
    else:
        if counter < 3:
            print("Try again!")
        else:
            print("Account unrecoverable")







vowels = ['a','e','i','o','u']
output = ""
phrase = input("Enter in a phrase and I'll remove the vowels: ")

#loop through all the letters and check if it is a vowel

for char in phrase:
    if char.lower() in vowels:
        char = " "
        output = output + char
    else:
        output = output + char
print(output)
'''

