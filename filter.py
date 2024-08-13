def filterEvenNumbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = [11, 12, 13,14, 15, 16, 17, 18, 19, 20]
even_numbers = filterEvenNumbers(numbers)

print(f"'this is the' {even_numbers}")