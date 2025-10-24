# Exercise 2 Shopping Cart Program
print(" \n===== Hello, this program calculates the price and quantity of things you bought! =====\n")

item = input("\nWhat item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"\nYou have bought {quantity} x {item}/s")
print(f"Your total is: R${total}")
print(" \n============== Thanks for using the program ==============\n")

