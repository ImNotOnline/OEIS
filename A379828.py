from collections import defaultdict

ulam_numbers_global = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102, 106, 114, 126, 131, 138, 145, 148, 155, 175, 177, 180, 182, 189, 197, 206, 209, 219, 221, 236, 238, 241, 243, 253, 258, 260, 273, 282, 309, 316, 319, 324, 339, 341, 356, 358, 362, 370, 382, 390, 400]

def generate_ulam_numbers(limit):
    ulam_numbers = [1, 2]  # Initialize with the first two Ulam numbers
    sums_count = defaultdict(int)

    # Precompute sums for the initial Ulam numbers
    sums_count[3] = 1

    candidate = 3  # Start from the first number after 1 and 2
    while candidate <= limit:
        if sums_count[candidate] == 1:
            ulam_numbers.append(candidate)
            for num in ulam_numbers[:-1]:
                new_sum = num + candidate
                if new_sum <= limit:  # Only consider sums within the limit
                    sums_count[new_sum] += 1
        candidate += 1

    return ulam_numbers




def is_ulam(n):
    global ulam_numbers_global  # Declare it as global to modify the global variable
    if n > ulam_numbers_global[-1]:
        ulam_numbers_global = generate_ulam_numbers(n)
    return n in ulam_numbers_global


def ulam_oblong():
    j = 0
    i = 1
    while True:
        oblong = i * (i + 1)
        if is_ulam(oblong):
            j += 1
            print(str(j) + str(" ") +  str(oblong))
        i += 1

# Example usage
c=0
ulam_oblong()


# Example usage
n = 5  # Find the 5th number satisfying the conditions
