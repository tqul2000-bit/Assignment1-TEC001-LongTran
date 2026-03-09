# Task 1
numbers = []
while True:
    num = input("Enter a number (press Enter to quit): ")
    if num == "":
        break
    numbers.append(float(num))
numbers.sort(reverse=True)
print("Five greatest numbers:")
for n in numbers[:5]:
    print(n)


# Task 2
seasons = ("winter", "spring", "summer", "autumn")
month = int(input("Enter month number (1-12): "))
season = seasons[(month % 12) // 3]
print("Season:", season)


# Task 3
names = set()
while True:
    name = input("Enter a name (press Enter to quit): ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
print("\nNames entered:")
for name in names:
    print(name)


# Task 4
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
text = input("Enter a piece of text: ")
frequencies = word_frequency(text)
print("Word frequencies:")
for word, count in frequencies.items():
    print(word, ":", count)


# Task 5
def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
original_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = remove_odd_numbers(original_list)
print("Original list:", original_list)
print("List without odd numbers:", new_list)


# Task 6
import random
points = int(input("How many random points to generate? "))
inside_circle = 0
for _ in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_circle += 1
pi_approx = 4 * inside_circle / points
print("Approximation of pi:", pi_approx)