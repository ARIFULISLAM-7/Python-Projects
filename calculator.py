operator = input("Enter an operator [+ - * /]:")
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

if operator == "+":
    result = number_1 + number_2
    print(result)
elif operator == "-":
    result = number_1 - number_2
    print(result)
elif operator == "*":
    result = number_1 * number_2
    print(result)
elif operator == "/":
    result = number_1 / number_2
    print(result)