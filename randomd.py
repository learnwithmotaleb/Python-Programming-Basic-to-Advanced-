import random

# Random integer between 1 and 10
print(random.randint(1, 10))

# Random float between 0 and 1
print(random.random())

# Random choice from a list
colors = ["Red", "Green", "Blue"]
print(random.choice(colors))

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
