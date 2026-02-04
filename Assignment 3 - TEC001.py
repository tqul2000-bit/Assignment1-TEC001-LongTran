#Task 1

num = 1

while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1

#Task 2

while True:
    inches = float(input("Enter inches (negative number to quit): "))

    if inches < 0:
        print("Program ended.")
        break

    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters} centimeters")

#Task 3

numbers = []

while True:
    user_input = input("Enter a number (press Enter to quit): ")

    if user_input == "":
        break

    number = float(user_input)
    numbers.append(number)

if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers were entered.")

#Task 4

import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break

#Task 5

correct_username = "python"
correct_password = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempts += 1
        print("Incorrect username or password.")

if attempts == max_attempts:
    print("Access denied")

#Task 6

def get_middle(text):
    length = len(text)
    middle = length // 2

    if length % 2 == 0:
        return text[middle - 1:middle + 1]
    else:
        return text[middle]

word = input("Enter a word: ")
result = get_middle(word)
print("Middle character(s):", result)

#Task 7

def make_acronym(phrase):
    words = phrase.split()
    acronym = ""

    for word in words:
        acronym += word[0].upper()

    return acronym

text = input("Enter a phrase: ")
result = make_acronym(text)
print("Acronym:", result)