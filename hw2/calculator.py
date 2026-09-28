first_number = float(input("Введіть перше число: "))
operation = input("Введіть дію (+, -, *, /): ").strip()
second_number = float(input("Введіть друге число: "))

if operation == "+":
    print("Результат:", first_number + second_number)
elif operation == "-":
    print("Результат:", first_number - second_number)
elif operation == "*":
    print("Результат:", first_number * second_number)
elif operation == "/":
    if second_number == 0:
        print("Помилка: ділити на нуль не можна!")
    else:
        print("Результат:", first_number / second_number)
else:
    print("Помилка: невідома дія!")
