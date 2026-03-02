#Task 1: Your university uses course codes that consist of 3 uppercase letters,
# followed by 3 digits (e.g., "TEC001").
# Write a function that returns True if a given string matches this format and False otherwise.

import re
def is_valid_course_code(code: str) -> bool:
    pattern = r'^[A-Z]{3}\d{3}$'
    return bool(re.match(pattern, code))
course_code = input("Enter a course code: ")
if is_valid_course_code(course_code):
    print("True")
else:
    print("False")

#Task 2: Web colors are often written in hexadecimal format:
# a # followed by exactly 6 characters (digits 0-9 or letters A-F, case insensitive).
# Write a function that checks if a given string is a valid hex color or not.

def is_valid_hex_color(color: str) -> bool:
    pattern = r'#[0-9a-fA-F]{6}$'
    return bool(re.match(pattern, color))

hex_color = input("Enter a hex color (e.g., #FFA07A): ")

print(is_valid_hex_color(hex_color))

#Task 3: Write a function that will find all numbers in a given paragraph,
# then calculate the sum of all numbers you've found. For example:
#    Input: "Today is January 16, 2025. The temperature is 11 degrees Celsius."
#    Output: 2052

def sum_numbers_in_text(text: str) -> int:
    numbers = re.findall(r'\d+', text)
    return sum(int(num) for num in numbers)
text = input("Enter a paragraph: ")
print(sum_numbers_in_text(text))

#Task 4: For privacy reasons, you need to hide phone numbers in a document.
# Write a function that replaces any sequence of 10 digits or those that starts with "+84" with the string [REDACTED].

def redact_phone_numbers(text: str) -> str:
    pattern = r'\b\d{10}\b|\+84\d+'
    return re.sub(pattern, '[REDACTED]', text)
text = input("Enter a document: ")
print(redact_phone_numbers(text))