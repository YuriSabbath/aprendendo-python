# Calculadora em Python

print(" \n===== Olá, esse programa é uma calculadora! =====\n")
operator = input("Digite um operador (+ - * /): ")
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
    print(" \n============== Obrigado por Utiliizar o programa ==============\n")
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
    print(" \n============== Obrigado por Utilizar o programa ==============\n")
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
    print(" \n============== Obrigado por Utiliizar o programa ==============\n")
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
    print(" \n============== Obrigado por Utiliizar o programa ==============\n")
else:
    print(f"{operator} is not a valid operator")
