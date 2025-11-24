# indexing = acessar partes de uma string usando [start:end:step]
# aqui usamos índices negativos para pegar os 4 últimos dígitos

credit_number = "1234-5678-9012-13456"

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
