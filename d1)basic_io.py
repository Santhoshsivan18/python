# The print() function is used to display output to the user.
print("Hello, World!")  # Output: Hello, World!

# The input() function is used to take input from the user.
name = input("Enter your name: ")  # Prompts user to enter their name
print("Hello, " + name)  # Greets the user with their name

# To read an integer input, use the int() function with input().
age = int(input("Enter your age: "))  # Converts the input string to an integer
print("You are " + str(age) + " years old.")  # Outputs the user's age

# To read a float input, use the float() function with input().
price = float(
    input("Enter the price of the item: ")
)  # Converts the input string to a float
print("The price is $" + str(price))  # Outputs the price

# 'end' parameter is used to specify what to print at the end. Default is newline.
print("Hello", end="==")  # Output: Hello (does not move to the next line)
print("World!")  # Output: World! (same line as Hello)
print("Hello")  # Output: Hello (does not move to the next line)
print("World!")  # Output: World! (same line as Hello)
print("Hello", end=" ")  # Output: Hello (does not move to the next line)
print("World!")  # Output: World! (same line as Hello)

# 'sep' parameter is used to specify separator between values.
print("Python", "is", "fun", sep="-")  # Output: Python-is-fun

# The format() method is used for formatting strings.
name = "Alice"
age = 25
print(
    "My name is {} and I am {} years old.".format(name, age)
)  # Output: My name is Alice and I am 25 years old.

# f-strings provide a concise and readable way to include expressions inside string literals.
name = "Alice"
age = 25
print(
    f"My name is {name} and I am {age} years old."
)  # Output: My name is Alice and I am 25 years old.
