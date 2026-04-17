def count_real_lines(filepath):
    count = 0
    try:
        with open(filepath, 'r') as file:
            for line in file:
                if line.strip():
                    count += 1

        print(f"Total number of non-blank lines: {count}")
        return count

    except FileNotFoundError:
        print("Error: The file does not exist.")
count_real_lines('r')