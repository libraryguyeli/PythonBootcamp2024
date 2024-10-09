import csv # A built-in Python module/library that allows us to work with CSV files

# Load text file
mailbox_file = open("mbox-short.txt")
emails = {} # Dictionary to store email addresses

# Loop through lines
"""
count = 0
for line in mailbox_file:
    # print(line)
    count += 1
print(f"Total lines: {count}")
"""

# Get 'from' email addresses
for line in mailbox_file:
    if line.startswith("From: "):
        # print(line)
        line_list = line.split() # Creates a list breaking at the spaces
        # print(line_list)
        email = line_list[1] # Just the email, not any preceding text

        # If the email is not in our dictionary, add that email key and a value of 1 to dictionary.
        # Else increase the count value by one.
        if email not in emails.keys():
            emails[email] = 1
        else:
            emails[email] += 1

print(emails)

# Going forward, all emails and their counts are stored in the dictionary 'emails'.
with open("emails.csv", "w", newline = "") as csvfile:
    fieldnames = ["Email", "Count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    # At this point, the only thing written is the header.
    # Below is writing all of the rows using keys and values from the dictionary 'emails'
    for e, c in emails.items():
        writer.writerow({"Email": e, "Count": c})


# Close the file!!! ALWAYS!
mailbox_file.close()
print("Finished")

