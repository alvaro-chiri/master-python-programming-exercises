# Accept a comma-separated input from the user
input_str = input("Enter a sequence of comma-separated numbers: ")

# Split the input string into a list of numbers
numbers = input_str.split(',')

# Convert the list of numbers to a tuple
numbers_tuple = tuple(numbers)


print("Tuple:", numbers_tuple)