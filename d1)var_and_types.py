# integers(whole nums)
num = 7
print(type(num))
print(num)
print()

# float(decimal nums)
fnum = 7.0  # or fnum = float(7)
print(type(fnum))
print(fnum)
print()

# string - single/double quotes
# The difference is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)
name = "hello guy's"  # or name = 'hello guys'
print(type(name))
print(name)
print()

# addition vs concatenation
num1 = 80
name1 = "how are u"
print(name + name1)
print(name + " " + name1)
print(num + num1)
# print(num + " " + num1) - TypeError
print()

# assignment operators
a, b, c = 1, 2, 3
d = e = f = 4
print(a + b + c + d)
print(str(a) + " " + str(b) + " " + str(c) + " " + str(d))
print()

# String Formatting
print("My name is {} and I'm {} years old.".format(name, num))  # Output: "My name is John and I'm 30 years old."
print(f"My name is {name} and I'm {num} years old.")  # Output: "My name is John and I'm 30 years old."