##### For Loops
backpack = ['phone', 'wallet', 'keys', 'book']
for item in backpack:
    print(item)
for number in range(10):
    print(number)


##### While Loops
i = 0
while True:
    i += 1
    print(i)
    if i == 5:
        break

username = input("Enter your username: ")
while username != "Eli":
    username = input("Enter your username: ")
print(f"Hello, {username}!")


##### Booleans
is_raining = False
borrow_pen = True
# while is_raining is False:
# while is_raining == False:
while not is_raining:
    rain = input("Is it raining? ")
    if rain == "y":
        is_raining = True

# while borrow_pen is True:
# while borrow_pen == True:
while borrow_pen:
    user_input = input("Take your pen back! ")
    if user_input == "y":
        borrow_pen = False
print("I took my pen back.")


##### Looping through dictionaries
eli = {
    "name": "Eli",
    "fav_color": "black",
    "fav_animal": "cats"
}
for item in eli.keys():
    print(f"{item}: {eli[item]}")
for item in eli.values():
    print(item)

print("Enter your grocery items.")
groceries = {}
while True:
    item = input()
    if item == "":
        break
    else:
        if item in groceries.keys():
            groceries[item] += 1
        else:
            groceries[item] = 1

for item in groceries.keys():
    print(f"{groceries[item]} {item.upper()}")


##### String slicing
today = "Today is Wednesday."
tomorrow = "Tomorrow is Thursday!"

bag = ["laptop","book","wallet"]

letters = {}

for char in today:
    if char in letters.keys():
        letters[char] += 1
    else:
        letters[char] = 1

print(letters)

