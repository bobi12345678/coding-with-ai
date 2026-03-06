def calculate_average(numbers):
    if not isinstance(numbers, list):  # Check if the input is not a list
        return "Error: Input must be a list of numbers."
    if not numbers:  # Check if the list is empty
        return 0
    return sum(numbers) / len(numbers)

# Example usage
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("The average is:", average)

# Example with invalid input
invalid_input = "not a list"
result = calculate_average(invalid_input)
print(result)

print(calculate_average('a'))