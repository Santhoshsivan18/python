print("Default arguments:\n")
def greet(name, message="Hello"):
    print(f"{message}, {name}!")
greet("John")
greet("Jane", "Goodbye")
print()

print("Keyword arguments:\n")
def person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")
person(name="John", age=30, city="New York")
print()

print("Arbitrary arguments:\n")
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_numbers(1, 2, 3, 4, 5))
print()

# Precedence order of the arguments - Positional > Default > Arbitrary positional(*args) > Arbitrary keyword(**kwargs)

def demonstrate_precedence(pos1, pos2, def1=10, def2=20, *args, **kwargs):
    print(f"Positional 1: {pos1}")
    print(f"Positional 2: {pos2}")
    print(f"Default 1: {def1}")
    print(f"Default 2: {def2}")
    print(f"Arbitrary Positional Arguments: {args}")
    print(f"Arbitrary Keyword Arguments: {kwargs}")

# Example function calls
print("Example 1:")
demonstrate_precedence(1, 2, 30, 40, "extra1", "extra2", key1="value1", key2="value2")

print("\nExample 2:")
demonstrate_precedence(1, 2, "extra1", "extra2", key1="value1", key2="value2")

print("\nExample 3:")
demonstrate_precedence(1, 2, key1="value1", key2="value2")


print("Default, Keyword & Arbitrary arguments:\n")
def create_profile(name, age=20, *hobbies, **additional_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Hobbies: {hobbies}")
    print(f"Additional Info: {additional_info}")
    print()

# Creating profiles
create_profile("Alice", 25, "Reading", "Traveling", city="New York", profession="Engineer")
create_profile("Bob0", "Hiking", "Cooking", country="USA")
create_profile("Bob1", 30, "Hiking", "Cooking", country="USA")
create_profile("Bob2", hobbies=("Hiking", "Cooking"), country="USA")
create_profile("Charlie", phone="123-456-7890", email="yours@example.com")

# *hobbies: Collects additional positional arguments into a tuple
# Alice - "Reading", "Traveling" are collected in hobbies tuple

# **additional_info: Collects additional keyword arguments into a dictionary
# Alice - city="New York", profession="Engineer" are collected in additional_info dictionary

# Default Argument: age=18 sets a default age
# Provides a fallback/default value if no argument is given

# Keyword Arguments: **additional_info allows additional key-value pairs
# Allows specifying arguments by name, making the function call more readable

# Arbitrary Argument: *hobbies allows multiple hobbies
# Handles variable numbers of arguments, offering flexibility

# Why Bob0 doesn't get the default age value?
# In the call create_profile("Bob0", "Hiking", "Cooking", country="USA"), Python assigns "Hiking" to age because the positional argument for age is provided immediately after the name. Python doesn't realize "Hiking" is a hobby because positional arguments take precedence over default and arbitrary arguments. Thus, the function interprets "Hiking" as age and assigns the rest to *hobbies.

# Why Bob2 prints the hobbies tuple in the print(f"Hobbies: {hobbies}") line?
# In the call create_profile("Bob2", hobbies=("Hiking", "Cooking"), country="USA"), you explicitly pass hobbies as a keyword argument (hobbies=("Hiking", "Cooking")). The function signature treats *hobbies as a positional argument for collecting extra arguments, not a named keyword argument. Since hobbies is passed as a keyword argument, it gets collected in **additional_info rather than *hobbies.
