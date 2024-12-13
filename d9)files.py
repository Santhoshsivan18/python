import os
import csv

# Creating files
text_file = 'example.txt'
binary_file = 'example.bin'
csv_file = 'example.csv'

open(text_file, 'w').close()
open(binary_file, 'wb').close()
open(csv_file, 'w', newline='').close()

# Writing to a Text File
text_content = "Hello, world!\nThis is a text file.\n"
with open(text_file, 'w') as file:
    file.write(text_content)

# Appending to a Text File
append_text = "Appending a new line.\n"
with open(text_file, 'a') as file:
    file.write(append_text)

# Reading from a Text File
with open(text_file, 'r') as file:
    content = file.read()
    print("Text File Content:\n", content)

# Writing to a Binary File
binary_data = b'Hello, binary world!'
with open(binary_file, 'wb') as file:
    file.write(binary_data)

# Reading from a Binary File
with open(binary_file, 'rb') as file:
    binary_content = file.read()
    print("Binary File Content:\n", binary_content)

# Writing to a CSV File
csv_data = [["Name", "Age", "City"], ["Alice", 30, "New York"], ["Bob", 25, "Los Angeles"]]
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

# Reading from a CSV File
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    print("CSV File Content:")
    for row in reader:
        print(row)

# Appending to a CSV File
append_csv_data = [["Charlie", 35, "Chicago"]]
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(append_csv_data)

# Verifying the Append Operation
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    print("Updated CSV File Content:")
    for row in reader:
        print(row)

# Deleting files
# os.remove(text_file)
# os.remove(binary_file)
# os.remove(csv_file)
