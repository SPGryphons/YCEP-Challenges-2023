import os

def count_subdirectories(path):
    """Return the number of subdirectories in the specified directory."""
    return sum(os.path.isdir(os.path.join(path, i)) for i in os.listdir(path))

# Get the current working directory
current_directory = os.getcwd()

# Get all the subdirectories in the current directory
subdirectories = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]

# Initialize a counter for the total number of subdirectories
total_subdirectories = 0

# Initialize a dictionary to hold the counts for each category
category_counts = {}

# Iterate over each subdirectory and count its subdirectories
for subdirectory in subdirectories:
    num_subdirectories = count_subdirectories(os.path.join(current_directory, subdirectory))
    total_subdirectories += num_subdirectories

    # Check if the subdirectory name matches a category and add the count to the category
    if subdirectory in category_counts:
        category_counts[subdirectory] += num_subdirectories
    else:
        category_counts[subdirectory] = num_subdirectories

# Print the results in a nicer format
print(f"{'Category':<10} | {'Subdirectory Count':<18}")
print('-' * 30)

for category, count in sorted(category_counts.items()):
    print(f"{category:<10} | {count:<18}")

print('-' * 30)
print(f"Total categories: {len(category_counts)}")
print(f"Total subdirectories: {total_subdirectories}")
