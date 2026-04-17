#Task 1
def count_non_empty_lines(file_path):
    count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    count += 1
        return count
    except FileNotFoundError:
        return "Error: The file was not found."
print(count_non_empty_lines('ddf.txt'))

#Task 2
def find_keyword_lines(file_path, keyword):
    line_numbers = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for current_line_num, content in enumerate(file, start=1):
                if keyword in content:
                    line_numbers.append(current_line_num)
        return line_numbers

    except FileNotFoundError:
        return "Error: File not found."
print(find_keyword_lines('text task 2.txt', 'A'))

#Task 3
def uppercase_file_converter(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as source:
            content = source.read()

        uppercased_content = content.upper()

        with open('output.txt', 'w', encoding='utf-8') as destination:
            destination.write(uppercased_content)
        print("Success! Result saved to output.txt")
    except FileNotFoundError:
        print("Error: The source file does not exist.")
uppercase_file_converter('text task 3.txt')

#Task 4
def calculate_average_score(file_path):
    total_score = 0
    student_count = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue

                parts = clean_line.split(',')
                if len(parts) == 2:
                    score = float(parts[1])
                    total_score += score
                    student_count += 1

        if student_count == 0:
            return 0
        return total_score / student_count

    except FileNotFoundError:
        return "Error: File not found."
    except ValueError:
        return "Error: File contains non-numeric scores."
print(calculate_average_score('text_task_4.txt'))