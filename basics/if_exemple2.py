# input + validação simples de string vazia
# if/else = executa caminhos diferentes conforme a condição

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

# checagem de estado booleano (online/offline)
online = True

if online:
    print("The user is online")
else:
    print("The user is offline")
