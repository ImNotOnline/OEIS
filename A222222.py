def swap_ones_and_fives(num):
    # Convert the number to a string for easy manipulation
    num_str = str(num)
    # Swap '1' and '5'
    swapped = ''.join('5' if digit == '1' else '1' if digit == '5' else digit for digit in num_str)
    # Convert back to an integer
    return int(swapped)

def write_swapped_numbers_to_file(x, filename="output.txt"):
    with open(filename, "w") as file:
        for num in range(0, x + 1):
            swapped = swap_ones_and_fives(num)
            file.write(f"{num} {swapped}\n")

# Example usage:
x = 9999  # Replace with your desired maximum value
write_swapped_numbers_to_file(x)
print("Numbers and their swapped counterparts have been written to 'output.txt'.")
