import sys
import math
import random

# Get data from the command line arguments
number = int(sys.argv[1])
text = sys.argv[2]

# Task 1: Number Puzzle
if number % 2 == 0:
    number_result = f"The number is even. Square root: {math.sqrt(number)}"
else:
    number_result = f"The number is odd. Cube: {number ** 3}"

# Task 2: Text Puzzle
binary_text = ' '.join(format(ord(char), '08b') for char in text)
vowel_count = sum(1 for char in text if char.lower() in 'aeiou')

# Task 3: Treasure Hunt
random_number = random.randint(1, 100)
attempts = 0
treasure_hunt_result = "You didn't win the treasure."

while attempts < 5:
    guess = random.randint(1, 100)  # Simulating guesses
    attempts += 1
    if guess == random_number:
        treasure_hunt_result = "Congratulations! You won the treasure!"
        break

# Display results
print(f"<p>{number_result}</p>")
print(f"<p>Binary-encoded text: {binary_text}</p>")
print(f"<p>Number of vowels in text: {vowel_count}</p>")
print(f"<p>{treasure_hunt_result}</p>")
