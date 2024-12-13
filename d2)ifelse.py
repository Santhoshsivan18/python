x = 2
print(x == 2)
print(x == 3)
print(x < 3)
print()
# The statements under if block is executed when the returned value is
# 1. The "True" boolean variable.
# 2. An object which is not considered "empty" is passed.

# The statements under else block is executed when the returned value is/The objects that re not considered empty are
# 1. An empty string: ""
# 2. An empty list: []
# 3. The number zero: 0
# 4. The false boolean variable: False

# Boolean operators - The "and" and "or" boolean operators allow building complex boolean expressions
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
if name == "John" or name == "Steven":
    print("Your name is either John or Rick.")
print()

# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
print()

# The "is" operator unlike the double equals operator "==" does not match the values of the variables, but the instances themselves.
# The is operator checks for identity equality. It checks whether the two variables point to the same object in memory.
# The == operator checks for value equality. It compares the values of the objects to determine if they are the same.
x = [1, 2, 3]
y = [1, 2, 3]
a = 5
b = 5
print("x == y : " + str(x == y))
print("x is y : " + str(x is y))
print("a == b : " + str(a == b))
print("a is b : " + str(a is b))
print()

# Using "not" operator before a boolean expression inverts it:
print(not False)
print((not False) == (False))
print()

