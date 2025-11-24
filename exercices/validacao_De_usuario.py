# validate user input exercise
# Regras:
# 1. O username deve ter no máximo 12 caracteres
# 2. Não pode conter espaços
# 3. Não pode conter dígitos (deve ser apenas letras)

username = input("Enter a username: ")

# Verificações básicas de validade
if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif username.find(" ") != -1:     # verifica se existe espaço
    print("Your username can't contain spaces")
elif not username.isalpha():       # garante que só há letras
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
