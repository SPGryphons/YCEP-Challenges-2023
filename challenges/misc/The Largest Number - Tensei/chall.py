import random

def generate_unique_numbers(num_count, file_path):
    numbers = set()

    # Generate unique random numbers
    while len(numbers) < num_count:
        numbers.add(random.randint(1, 9873451765489))

    # Write to txt file
    with open(file_path, 'a') as file:
        for number in numbers:
            file.write(str(number) + '\n')

#Call Function
generate_unique_numbers(1435737, 'chall.txt')