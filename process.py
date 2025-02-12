import sys
import random

if len(sys.argv) < 3:
    print("Error: Se requieren un número y un texto.")
    sys.exit(1)

user_number = int(sys.argv[1])
user_text = sys.argv[2]

if user_number % 2 == 0:
    number_result = f"The number {user_number} is even. Its square root is {user_number ** 0.5:.2f}."
else:
    number_result = f"The number {user_number} is odd. Its cube is {user_number ** 3}."

binary_text = " ".join(format(ord(c), "08b") for c in user_text)
vowel_count = sum(1 for c in user_text.lower() if c in "aeiou")

text_result = f"Binary: {binary_text}\nVowel Count: {vowel_count}"

secret_number = random.randint(1, 100)
attempts = 0
user_guess = random.randint(1, 100)

while user_guess != secret_number and attempts < 5:
    user_guess = random.randint(1, 100)
    attempts += 1

if user_guess == secret_number:
    treasure_result = f"You found the treasure in {attempts} attempts!"
else:
    treasure_result = "You did not find the treasure."

print(number_result)
print(text_result)
print(treasure_result)