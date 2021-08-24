import pandas as pandas
import sys as sys

if(len(sys.argv) < 3):
    print("Missing required absoluteFilePath or email column arguments")
    print("Please run as python3 csvEmailValidator.py [absoluteFilePath] [fieldColumn]")
    exit()

print("------ Starting processing of csv file ------")
print("Using file path " + sys.argv[1])
print("Using column number " + sys.argv[2])
print("\n")

try:
    absolute_file_path = sys.argv[1]
    field_column = int(sys.argv[2])

    csv_file = pandas.read_csv(absolute_file_path)
    csv_values = csv_file.values
    emails = set()

    for row in csv_values:
        email_address = row[field_column]
        if(emails.__contains__(email_address)):
            print("Conflicting column with value as: " + email_address)
        else:
            emails.add(email_address)

except FileNotFoundError:
    print("Could not find document for path " + sys.argv[1])
    print("Please provide absolute path to file")
except (IndexError, ValueError): 
    print("Field column number is not valid " + sys.argv[2])
    print("Please provide a valid column number from the file: from 0 to n")

