# num pad layout = imprime uma matriz representando um teclado numérico

num_pad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
)

# percorre linha por linha e imprime cada elemento no mesmo formato do keypad
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
