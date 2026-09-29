numbers = [0, 1, 7, 2, 4, 8]

if numbers:
    result = sum(numbers[::2]) * numbers[-1]
else:
    result = 0

print(result)
