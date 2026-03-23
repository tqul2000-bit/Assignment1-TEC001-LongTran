#Task 1
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Please enter a valid number.")
numbers.sort(reverse=True)
print("\nThe five greatest numbers in descending order are:")
for n in numbers[:5]:
    print(n)

#Task 2
try:
    num = int(input("Enter an integer: "))

    if num <= 1:
        print(f"{num} is not a prime number.")
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")

except ValueError:
    print("Please enter a valid integer.")

#Task 3
cities = []
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)

print("\nThe cities you entered are:")

for city in cities:
    print(city)

#Task 4
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_numbers = [10, 20, 30, 40, 50]
result = sum_list(my_numbers)

print(f"The list is: {my_numbers}")
print(f"The sum is: {result}")

#Task 5
def remove_odd_numbers(original_list):
    even_numbers = []
    for num in original_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = remove_odd_numbers(my_list)

print(f"Original list: {my_list}")
print(f"Cut-down list (evens only): {filtered_list}")