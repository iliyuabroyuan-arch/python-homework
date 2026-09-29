numbers = [0, 1, 0, 12, 3]

zero_count = numbers.count(0)
numbers[:] = [number for number in numbers if number != 0]
numbers.extend([0] * zero_count)

print(numbers)
