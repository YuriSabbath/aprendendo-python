# Temperature Conversion Program

print(" \n===== Hello, this program converts temperature! =====\n")

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").upper()
temp = float(input("Enter the temperatue: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
    print(" \n===== Thanks for using the program! =====\n")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
    print(" \n===== Thanks for using the program! =====\n")
else:
    print(f"{unit} is an invalid unit of measurement")