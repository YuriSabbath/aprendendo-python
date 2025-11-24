# exercise 2 = cálculo do total de um carrinho de compras simples

print("\n===== Shopping Cart Calculator =====\n")

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"\nYou bought {quantity}x {item}(s)")
print(f"Your total is: R${total}")
print("\n============== End of Program ==============\n")
