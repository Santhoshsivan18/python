print("Recursive Functions:")


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of a num :", factorial(5))
# The function calls itself with n-1 until n is 1.
# When n is 1, it returns 1, unwinding the recursive calls to get the final result.


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Sum of Fibonacci series :", fibonacci(10))
# The function calls itself twice to calculate the nth Fibonacci number.
# For n <= 0, it returns 0; for n == 1, it returns 1.
# For all other cases, it returns the sum of the two preceding Fibonacci numbers.

print()
print("Lambda Functions:")
add = lambda x, y: x + y
print("Sum of x & y : ", add(2, 3))
# A lambda function is defined to add two numbers.
# The add function takes two arguments, x and y, and returns their sum.
students = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 22},
    {"name": "Dave", "age": 20},
]
# Sort the list of dictionaries by age using a lambda function
print(sorted(students, key=lambda student: student["age"]))
# A list of dictionaries representing students is defined.
# The sorted function is used to sort the list by the age key.
# A lambda function is used as the key to extract the age value from each dictionary for sorting.
