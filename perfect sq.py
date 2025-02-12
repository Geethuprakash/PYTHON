def is_all_even_digits(num):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True

def find_perfect_squares_with_even_digits():
    result = []
    for num in range(1000, 2000):
        square = num * num
        if is_all_even_digits(square):
            result.append(square)
    return result

perfect_squares = find_perfect_squares_with_even_digits()
print(perfect_squares)