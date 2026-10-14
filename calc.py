while True:
    num1 = float(input("Введи первое число: "))
    operation = input("Выбери действие (+, -, *, /):")
    if operation == "exit":
        print ("Пока!")
        break
    num2 = float(input("Введи второе число: "))
    if operation == "+":
        result = num1 + num2
    if operation == "-":
        result = num1 - num2
    if operation == "*":
        result = num1 * num2
    if operation == "/":
        result = num1 / num2
    print (result)
