# List example
fruits = ['apple', 'banana', 'cherry', 'date']

# Basic access
print(fruits[0])  # Outputs: apple
print(fruits[1])  # Outputs: banana

# Negative indices
print(fruits[-1])  # Outputs: date
print(fruits[-2])  # Outputs: cherry

# Slicing
print(fruits[1:3])  # Outputs: ['banana', 'cherry']
print(fruits[:2])  # Outputs: ['apple', 'banana']
print(fruits[2:])  # Outputs: ['cherry', 'date']

# Stepping
print(fruits[0:4:2])  # Outputs: ['apple', 'cherry']

# Using enumerate()
for index, value in enumerate(fruits):
    print(f'Index {index} contains {value}')

# List Examples
print("List Examples :")
# my_list = ["1, 2, 3, 4, 5"]
my_list = ["a", "b", "c", "d", "e"]

# my_list.append(6)
my_list.append("f")
print("After append:", my_list)

# my_list.extend([7, 8, 9])
my_list.extend(["g", "h", "i"])
print("After extend:", my_list)

my_list.insert(3, "inserted")
print("After insert:", my_list)

my_list.remove("inserted")
print("After remove:", my_list)

popped_element = my_list.pop()
print("After pop:", my_list, "; Popped element:", popped_element)

# index_of_2 = my_list.index(2)
index_of_2 = my_list.index("c")
print("Index of first occurrence of 2:", index_of_2)

# count_of_2 = my_list.count(2)
count_of_2 = my_list.count("c")
print("Count of 2:", count_of_2)

my_list.sort()
print("After sort:", my_list)

my_list.reverse()
print("After reverse:", my_list)

copied_list = my_list.copy()
print("Copied list:", copied_list)

my_list.clear()
print("After clear:", my_list)

print("\n")

# Tuple Examples
print("Tuple Examples :")
my_tuple = (1, 2, 3, 2, 4, 2, -5)

# Tuple example
fruits = ('apple', 'banana', 'cherry', 'date')

# Basic access
print(fruits[0])  # Outputs: apple
print(fruits[1])  # Outputs: banana

# Negative indices
print(fruits[-1])  # Outputs: date
print(fruits[-2])  # Outputs: cherry

# Slicing
print(fruits[1:3])  # Outputs: ('banana', 'cherry')
print(fruits[:2])  # Outputs: ('apple', 'banana')
print(fruits[2:])  # Outputs: ('cherry', 'date')

# Stepping
print(fruits[0:4:2])  # Outputs: ('apple', 'cherry')

# Using enumerate()
for index, value in enumerate(fruits):
    print(f'Index {index} contains {value}')


count_of_2 = my_tuple.count(2)
print("Count of 2 in tuple:", count_of_2)

index_of_2 = my_tuple.index(2)
print("Index of first occurrence of 2 in tuple:", index_of_2)

my_tuple = (1, 2, 3)
print("Second element of tuple:", my_tuple[1])

my_tuple = (1, 2, 3, 4, 5)
print("Slice of tuple (1:4):", my_tuple[1:4])

tuple1 = (1, 2)
tuple2 = (3, 4)
combined_tuple = tuple1 + tuple2
print("Concatenation:", combined_tuple)

my_tuple = (1, 2)
repeated_tuple = my_tuple * 3
print("Repetition:", repeated_tuple)

my_tuple = (1, 2, 3)
print("Check if element is present (2):", 2 in my_tuple)

my_tuple = (1, 2, 3)
print("Deleting a tuple:")
del my_tuple
# print(my_tuple)

print("\n")

print("Stack implementation:")
stack = []

# Adding elements to stack
stack.append(1)
print(f"Element 1 pushed to stack.")
stack.append(2)
print(f"Element 2 pushed to stack.")
stack.append(3)
print(f"Element 3 pushed to stack.")

# Display the stack
print("Stack contents:", stack)

# Peek at the top element of the stack
if len(stack) > 0:  # Check if stack is not empty
    print(f"Top element is {stack[-1]}.")
else:
    print("Stack is empty.")

# Pop elements from the stack
if len(stack) > 0:  # Check if stack is not empty before popping
    print(f"Element {stack.pop()} popped from stack.")
else:
    print("Stack is empty.")

if len(stack) > 0:
    print(f"Element {stack.pop()} popped from stack.")
else:
    print("Stack is empty.")

# Display the stack after popping
print("Stack contents:", stack)

# Check if the stack is empty
print("Is stack empty ?", len(stack) == 0)

# Get the size of the stack
print("Stack size:", len(stack))

# Pop remaining elements
for i in range(0, len(stack)):
    if len(stack) > 0:
        print(f"Element {stack.pop()} popped from stack.")
    else:
        print("Stack is empty.")

if len(stack) > 0:
    print(f"Element {stack.pop()} popped from stack.")
else:
    print("Stack is empty.")  # Trying to pop from an empty stack

# Display the stack contents
print("Stack contents:", stack)

print("\n")

print("Queue implementation:")
from collections import deque

# Initialize an empty queue
queue = deque()

# Enqueue elements to the queue
queue.append(1)
print(f"Element 1 enqueued to queue.")
queue.append(2)
print(f"Element 2 enqueued to queue.")
queue.appendleft(20)
print(f"Element 20 enqueued to queue.")
queue.appendleft(30)
print(f"Element 20 enqueued to queue.")
queue.append(3)
print(f"Element 3 enqueued to queue.")
queue.append(3)
print(f"Element 3 enqueued to queue.")

# Display the queue
print("Queue contents as deque:", queue)
print("Queue contents as list:", list(queue))

# Peek at the front element of the queue
if len(queue) > 0:  # Check if queue is not empty
    print(f"Front element is {queue[0]}.")
else:
    print("Queue is empty.")

# Dequeue elements from the queue
if len(queue) > 0:  # Check if queue is not empty before dequeuing
    print(f"Element {queue.popleft()} removed from the front/dequeued from queue.")
else:
    print("Queue is empty.")

if len(queue) > 0:
    print(f"Element {queue.pop()} removed from the end/dequeued from queue.")
else:
    print("Queue is empty.")

# Display the queue contents after dequeuing
print("Queue contents:", list(queue))

# Check if the queue is empty
print("Is queue empty?", len(queue) == 0)

# Get the size of the queue
print("Queue size:", len(queue))

# Insert element at specific position
queue.insert(1, 99)
print("Element 99 inserted at index 1.")
print("Queue contents after insertion:", list(queue))

# Count occurrences of an element
count_2 = queue.count(2)
print(f"Element 2 occurs {count_2} times in the queue.")

# Remove specific element
queue.remove(99)
print("Element 99 removed from the queue.")
print("Queue contents after removal:", list(queue))

# Extend the queue with iterable
queue.extend([4, 5, 6])
print("Queue extended with [4, 5, 6].")
print("Queue contents:", list(queue))

# Extendleft the queue with iterable
queue.extendleft([7, 8, 9])
print("Queue extended to the left with [7, 8, 9].")
print("Queue contents:", list(queue))

# Reverse the queue
queue.reverse()
print("Reversed Queue contents:", list(queue))

# Rotate the queue
queue.rotate(2)  # Rotate to the right by 2 positions
print("Queue rotated to the right by 2 positions.")
print("Queue contents:", list(queue))

# Dequeue remaining elements
while len(queue) > 0:
    print(f"Element {queue.popleft()} dequeued from queue.")

# Display the queue contents
print("Queue contents:", list(queue))
