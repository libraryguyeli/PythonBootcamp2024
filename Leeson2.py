# Game Plan

# In-Class Review Assignment



# Write a program that prompts the user to enter the number of hours they work, their
# hourly rate and then returns their gross pay
'''
# TO DO Prompt for hours worked
hours_worked = float(input("How many hours did you work?"))

# TO DO Prompt for their hourly rate
hourly_rate = float(input("What is your hourly rate?"))

# TO DO Math... hours worked * hourly rate
gross_pay = hours_worked * hourly_rate

# TO DO Present Answer
print(gross_pay)
'''
# Example of creating a function that would print the same answer. The parameters hours_worked and hourly_rate
# although not technically variables, work like variables by capturing the values that the user enters
def gross_pay_calc(hours_worked,hourly_rate):
    print( hours_worked * hourly_rate)

# Uncomment line 28 to call the gross_pay_calc function with 40 as hours_worked and 15 as hourly_rate
#gross_pay_calc(40,15)

# Example of another function that works the same way; however, no parameters are needed. The hours_worked and
# and hourly_rate will be input by the user.
def gross_pay_2():
    hours_worked = float(input("How many hours did you work?"))
    hourly_rate = float(input("What is your hourly rate?"))
    print(hourly_rate * hours_worked)

# Uncomment line 38 to call the gross_pay_2() function. Eventhough there are no parameters, the parenthesis
# must still be typed.
#gross_pay_2()

# Conditional Lesson
'''
# Your conditional test is lines 46 - 55.
age = int(input("How old are you?"))

if age > 100:
    print("Probably shouldn't get a license")
elif age >= 16:
    print("You are eligible for a drivers license")
elif age < 0:
    print("Not a valid age")

else:
    print("You are not old enough for a license")

print("Code Complete")

# Another example of a conditional; however, this checks to see if a string matches the content in the variable
stop_light = "blue"

if stop_light == "green":
    print("Go!")
elif stop_light == "red":
    print("Stop")
else:
    print("Not a valid color")

# Example of a boolean conditional which checks if the is_raining variable is True or False
# and return accordingly
is_raining = False

if is_raining == False:
    print("You do not need an umbrella")
else:
    print("You need an umbrella")

is_raining = True

print(is_raining)

# Example of a list data type and how to remove and add elements from a list
backpack = ["phone", "keys","book"]

print(backpack)

print("You dropped your phone...oh no..")

backpack.remove("phone")

print(backpack)

# Conditional checking if a string is in the list
if "phone" in backpack:
    print("Awesome. Leave the house.")
else:
    print("You forgot your phone")

print("You found a piece of gold on the ground and added it to your backpack")
backpack.append("Piece of Gold")

print(backpack)
'''


# In-Class Assignment

# Write a program that prompts the user to enter the number of hours they
# work, their hourly rate and then returns their gross pay; however, consider 
# that if over 40 hours are worked, each hour over 40 should be calculated at 1.5 times pay.
'''
hours_worked = float(input("How many hours were worked?"))
hourly_rate = float(input("What is the rate of pay?"))

if hours_worked >= 40:
    extra_hours = hours_worked - 40
    print((extra_hours * (hourly_rate * 1.5)) + (40 * hourly_rate))
else:
    print(hourly_rate * hours_worked)
'''
