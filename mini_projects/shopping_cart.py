# Shopping cart program

foods = []          # Lista de itens adicionados ao carrinho
prices = []         # Lista dos preços correspondentes
total = 0           # Total acumulado

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":         # Encerra o programa
        break
    else:
        price = float(input(f"Enter the price of a {food}: R$"))
        foods.append(food)          # Armazena o item
        prices.append(price)        # Armazena o preço

print("\n----- YOUR CART -----")

for food in foods:
    print(food)                     # Exibe todos os itens

for price in prices:
    total = total + price           # Soma dos preços

print(f"\nYour total is: R${total}")
