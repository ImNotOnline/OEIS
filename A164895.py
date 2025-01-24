import mpmath
from mpmath import mp

def pi_digits_to_binary(n):
    """
    Calculate the first n digits of pi (including the digit before the decimal point),
    convert each digit to binary, and concatenate them into a single binary string.

    Args:
        n (int): Number of digits of pi to calculate (including the integer part).

    Returns:
        str: Concatenated binary representation of the digits of pi.
    """
    if n <= 0:
        raise ValueError("The number of digits must be greater than 0.")

    # Set the precision for mpmath to ensure we calculate enough digits
    mp.dps = n + 1  # Extra digit to account for rounding
    pi_str = str(mp.pi).replace('.', '')[:n]  # Extract the first n digits including the integer part

    binary_string = "".join(bin(int(digit))[2:] for digit in pi_str)
    return binary_string
def binaryToDecimal(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

# Example usage
#while True:
#    n = int(input("Input n: "))
#    print(f"The first {n} digits of pi in binary: {binaryToDecimal(int(pi_digits_to_binary(n)))}")
def write_numbers_and_function_to_file(x, filename):
    """
    Writes numbers from 1 to x and the result of a function applied to each number to a file.

    Args:
        x (int): The upper limit of numbers to write.
        filename (str): The name of the file to write the data to.
    """

    with open(filename, 'w') as file:
        for n in range(1, x + 1):
            result = binaryToDecimal(int(pi_digits_to_binary(n)))
            file.write(f"{n} {result}\n")

# Example usage
while True:
    x = input("Up to n: ")
    write_numbers_and_function_to_file(int(x), 'output.txt')
    print(binaryToDecimal(int(pi_digits_to_binary(int(x)))))
