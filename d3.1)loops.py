# for loops iterate over a given sequence
print("for loop")
for x in range(5):
    print(x, end=" ")
print()
for x in range(3, 6):
    print(x, end=" ")
print()
for x in range(3, 8, 2):
    print(x, end=" ")
print()
print()

# while loops repeat as long as a certain boolean condition is met
print("while loop")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()
print()

# break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" loop start to execute the next iteration statement
print("break & continue")
count = 0
while True:
    print(count, end=" ")
    count += 1
    if count >= 8:
        break
print()

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    print("x % 2 : ", x % 2)
    if x % 2 == 0:
        continue
        print("if is true")
    print("if is false")
    print(x, end=" ")
print()
print()

# In python else condition can be used with for/while loops
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
else:
    print("count value reached %d" % (count))

for i in range(1, 10):
    if i % 5 == 0:
        # break
        continue
    print(i, end=" ")
else:
    print(
        "this is not printed because for loop is terminated because of break but not due to fail in condition"
    )

print()

# Using break and continue in a for loop
print("For Loop Example with Break and Continue:")
for i in range(1, 11):
    if i == 3:
        print("Skipping number 3")
        continue  # Skip the rest of the code in this iteration for i == 3
    if i == 5:
        print("Skipping number 5")
        continue  # Skip the rest of the code in this iteration for i == 5
    if i == 8:
        print("Breaking at number 8")
        break  # Exit the loop when i is 8
    print(i)


# Using break and continue in a while loop
print("\nWhile Loop Example with Break and Continue:")
i = 1
while i <= 10:
    if i == 2:
        print("Skipping number 2")
        i += 1
        continue  # Skip the rest of the code in this iteration for i == 2
    if i == 4:
        print("Skipping number 4")
        i += 1
        continue  # Skip the rest of the code in this iteration for i == 4
    if i == 7:
        print("Breaking at number 7")
        break  # Exit the loop when i is 7
    print(i)
    i += 1
