# nested loop = um loop dentro de outro; o externo controla as linhas e o interno controla as colunas

# Coleta de parâmetros para construir a grade
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

# Gera uma grade usando loops aninhados
for x in range(rows):          # loop externo → linhas
    for y in range(columns):   # loop interno → colunas
        print(symbol, end="")
    print()
