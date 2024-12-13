print("Errors")
# print("Hello, world!")
# print(10/0)

print("Assert")
x = 5
y = 10
# assert y != 0, "y should not be zero"
result = x / y

x = "welcome"
assert x != "hello", "x should be 'hello'"
# assert x == "hello", "x should be 'hello'"


print("Exception handling using try, except and finally")
try:
    # Outer try block to handle broader exceptions
    try:
        # Inner try block for more specific operations
        num = int(input("Enter a number: "))

        try:
            result = 10 / num
            print("Result:", result)
        except ZeroDivisionError as e:
            print("\nError: Division by zero is not allowed. Original exception:\n", e)

    except ValueError as e:
        print(
            "\nError: Invalid input. Please enter a valid number. Original exception:\n", e
        )

    # Simulate another potential error
    try:
        data = {"key1": "value1"}
        print(data["key2"])  # This will raise a KeyError
    except KeyError as e:
        print("\nError: The key does not exist in the dictionary. Original exception:\n", e)

except Exception as e:
    # Handle any other exceptions
    print("\nAn unexpected error occurred:\n", e)
finally:
    # Code that will run regardless of whether an exception was raised or not
    print("Execution complete.")
