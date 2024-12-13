# Initialize dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"],
}
print("Original dictionary:\n", thisdict, "\n")

# Access Items
print("Access 'brand':", thisdict["brand"])  # Using the key
print("Access 'model' with get():", thisdict.get("model"), "\n")

# Change & Add Items
thisdict["year"] = 2020  # Changing an existing value
thisdict["electric"] = True  # Adding a new key-value pair
print("Dictionary after changing 'year' & adding 'electric':\n", thisdict, "\n")

# Remove Items
thisdict.pop("model")  # Remove item by key
print("Dictionary after popping 'model':\n", thisdict, "\n")

thisdict.popitem()  # Remove the last inserted item
print("Dictionary after popitem:\n", thisdict, "\n")

del thisdict["year"]  # Remove item by key using del
print("Dictionary after deleting 'year':\n", thisdict, "\n")

# Loop Through a Dictionary
print("Looping through keys and values:")
for key, value in thisdict.items():
    print(f"{key}: {value}")
print()

print("Looping through keys:")
for key in thisdict.keys():
    print(f"{key}")
print()

print("Looping through values:")
for value in thisdict.values():
    print(f"{value}")
print()

# Copy Dictionary
thisdict_copy = thisdict.copy()  # Copy using copy method
print("Copied dictionary:", thisdict_copy, "\n")

# Nested Dictionary
nested_dict = {
    "child1": {"name": "Emily", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}
print("Nested dictionary:", nested_dict, "\n")

for x, obj in nested_dict.items():
    print(x)
    for y in obj:
        print(f"<{y}: {obj[y]}>")
    print()

# Dictionary Methods
print("Dictionary methods:")

# clear()
sample_dict = {"a": 1, "b": 2, "c": 3}
sample_dict.clear()
print("Dictionary after clear():", sample_dict, "\n")

# fromkeys()
keys = ("key1", "key2", "key3")
value = 0
new_dict = dict.fromkeys(keys, value)
print("New dictionary from keys:", new_dict, "\n")

# items()
print("Items in thisdict:", list(thisdict.items()), "\n")

# keys()
print("Keys in thisdict:", list(thisdict.keys()), "\n")

# values()
print("Values in thisdict:", list(thisdict.values()), "\n")

thisdict3 = {
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"],
}

# setdefault() - Combines the functionality of retrieving a value and adding a key-value pair if the key is missing.
thisdict3.setdefault("brand", "Audi")
print("Dictionary after setdefault 'brand':", thisdict3, "\n")

# update()
thisdict.update({"year": 2025})
print("Dictionary after update 'year':", thisdict, "\n")
