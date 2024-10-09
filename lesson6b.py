import csv # A built-in Python module/library that allows us to work with CSV files

# Load text file
mailbox_file = open("mbox-short.txt")
domains = {} # Dictionary to store email addresses
print("Process started. Please wait...")

# Get 'from' email addresses
for line in mailbox_file:
    if line.startswith("From: "):
        line_list = line.split() # Creates a list breaking at the spaces
        email = line_list[1] # Just the email, not any preceding text
        domain_email = email[email.rfind("@")+1:]

        if domain_email not in domains.keys():
            domains[domain_email] = 1
        else:
            domains[domain_email] += 1


with open("domains.csv", "w", newline = "") as csvfile:
    fieldnames = ["Domain", "Count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for d, c in domains.items():
        writer.writerow({"Domain": d, "Count": c})

print("Finished")