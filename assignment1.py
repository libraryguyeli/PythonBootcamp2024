"""
Assignment 1: Wednesday, September 11th
"""

# Ask the user for their name (str) and age (int)
name = input("What's your name? ")
age = int(input("How old are you? "))
# Print the name and age + 100 in a formatted string
print(f"Hi, {name}! In 100 years, you will be {age + 100}.")


# Print an empty line to space out my answers
print()


# Define a new function that takes parameters for cost of meal and desired tip percentage
def tip_calculator(meal_cost, tip_percentage):
    # Convert the tip percentage to a floating point number that can be multiplied with the meal cost
    tip_percentage = tip_percentage * 0.01
    # Calculate the total tip by multiplying tip rate with cost of meal
    total_tip = tip_percentage * meal_cost
    # Calculate total cost by adding tip and meal cost
    total_cost = total_tip + meal_cost
    # Return the total cost and total tip to the function call
    return total_cost, total_tip

# Ask the user for meal cost, convert to float
meal_cost = float(input("How much was your meal? "))
# Ask the user what percentage to tip, convert to integer (whole number)
tip_perc = int(input("What percentage will you tip? "))
# Assign the return values of the tip_calculator function to two variables respectively
total_cost, total_tip = tip_calculator(meal_cost, tip_perc)
# Print a formatted string showing the calculated tip and total cost including tip
print(f"You should tip ${total_tip:.2f} for a total cost of ${total_cost:.2f}.")
