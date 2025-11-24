# Calculadora simples
# O usuário escolhe um operador e insere dois números.
# O programa realiza a operação e exibe o resultado arredondado.

print(" \n===== Olá, esse programa é uma calculadora! =====\n")

operator = input("Digite um operador (+ - * /): ")
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

# Verifica o operador escolhido e executa a operação correspondente
if operator == "+":
    result = num1 + num2
    print(round(result, 3))
    print(" \n============== Obrigado por Utilizar o programa ==============\n")

elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
    print(" \n============== Obrigado por Utilizar o programa ==============\n")

elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
    print(" \n============== Obrigado por Utilizar o programa ==============\n")

elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
    print(" \n====
