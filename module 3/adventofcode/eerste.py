# Input string


# Split the string into two arrays: left and right
numbers = list(map(int, input_string.split(',')))
mid_index = len(numbers) // 2
left_array = numbers[:mid_index]
right_array = numbers[mid_index:]

# Extract the first elements from both arrays
left_first = left_array[0]
right_first = right_array[0]

# Determine the order
if left_first > right_first:
    result = f"{left_first}-{right_first}"
else:
    result = f"{right_first}-{left_first}"

print("Result:", result)
