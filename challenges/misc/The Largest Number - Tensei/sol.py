def find_largest_number(file_path):
    largest_number = None

    # Read from txt file
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            if largest_number is None or number > largest_number:
                largest_number = number

    return largest_number

# Call Function
largest_number = find_largest_number('chall.txt')
print("The largest number is:", largest_number)