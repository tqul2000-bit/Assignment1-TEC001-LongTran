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