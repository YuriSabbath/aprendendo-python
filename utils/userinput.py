# input() = função que solicita entrada do usuário
#           sempre retorna o valor como string

name = input("What is your name?: ")
age = int(input("How old are you?: "))   # conversão direta para int

# Também poderia ser assim (via typecasting):
# age = int(age)

age = age + 1   # incrementa idade

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old")
