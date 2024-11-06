"""
Assignment 3: Wednesday, September 25th
"""

def remove_vowels(sentence):
  # Put all vowels upper and lower in a list
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  new_sentence = ""
  for char in sentence:
    if char in vowels:
      continue # If the char is in the list, skip it
    else:
      new_sentence += char # If the char is not in the list, add it to new sentence
  return new_sentence


def validate_password(password):
  # Dictionary of password requirements to keep track of how the user completes the password
  requirements = {
    'upper': 0,
    'lower': 0,
    'numeric': 0,
    'special': 0
  }
  # If the length is less than 8 characters, automatically ask for another password.
  # Otherwise, keep going.
  if len(password) >= 8:
    pass
  else:
    return False
  # Loop through each char in the password and check if it is one of the following.
  for char in password:
    if char.isupper():
      requirements['upper'] += 1
    elif char.islower():
      requirements['lower'] += 1
    elif char.isnumeric():
      requirements['numeric'] += 1
    elif char.isspace():
      return False
    # If it is not upper, lower, number, or space, it must be a special character.
    else:
      requirements['special'] += 1
  # If all requirements are met (all dict values above 0), it meets all requirements.
  if requirements['upper'] > 0 and requirements['lower'] > 0 and requirements['numeric'] > 0 and requirements['special'] > 0:
    return True
  else:
    return False


# Assignment 3A
sentence = input("Enter a sentence: ")
vowels_removed = remove_vowels(sentence)
print(f"No vowels: {vowels_removed}")


# Print an empty line to separate assignments
print()


# Assignment 3B
password_valid = False # Start off with an invalid password because the user hasn't entered anything
while password_valid is False:
  print("Password requirements:\n1 uppercase letter\n1 lowercase letter\n1 number\n1 special character\n8 characters long\nNO SPACES\n")
  user_password = input("Enter a password: ")
  # Change the password_valid variable to either True (requirements met) or False (not met) which is determined by the function
  # If password_valid is True, the loop ends and it prints the last line, which is outside of the loop.
  password_valid = validate_password(user_password)
print("Thank you for entering a password.")