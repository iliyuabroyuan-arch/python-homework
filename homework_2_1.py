
number = float(input("Введіть число: "))
print("Квадрат числа:", number ** 2)

first = float(input("Введіть перше число: "))
second = float(input("Введіть друге число: "))
third = float(input("Введіть третє число: "))
average = (first + second + third) / 3
print("Середнє:", average)

total_minutes = int(input("Введіть кількість хвилин: "))
hours = total_minutes // 60
minutes = total_minutes % 60
print(hours, "години", minutes, "хвилин")

price = float(input("Введіть ціну: "))
discount = float(input("Введіть знижку (%): "))
final_price = price * (1 - discount / 100)
print("Ціна зі знижкою:", final_price)

number = int(input("Введіть ціле число: "))
print("Остання цифра:", abs(number) % 10)

length = float(input("Введіть довжину: "))
width = float(input("Введіть ширину: "))
perimeter = 2 * (length + width)
print("Периметр:", perimeter)

number = abs(int(input("Введіть чотиризначне ціле число: ")))
print(number // 1000)
print(number // 100 % 10)
print(number // 10 % 10)
print(number % 10)
