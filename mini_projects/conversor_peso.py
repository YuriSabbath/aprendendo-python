# Conversor de peso
# Converte entre quilos (K) e libras (L) dependendo da escolha do usuário.

print(" \n===== Hello, this program converts your weight! =====\n")

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

# Verifica a unidade inserida e realiza a conversão
if unit == "K":
    weight = weight * 2.205      # kg → lbs
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")

elif unit == "L":
    weight = weight / 2.205      # lbs → kg
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")

else:
    print(f"{unit} was not valid")

print(" \n============== Thanks for using the program! ==============\n")
