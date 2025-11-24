# Dictionary = coleção de pares {chave: valor}
#              ordenado, mutável e sem duplicatas de chave.

# Dicionário de países e capitais
capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# Exemplos úteis (referência):
# print(dir(capitals))           # lista métodos disponíveis do dict
# print(help(capitals))          # documentação completa
# print(capitals.get("India"))   # acessa valor sem risco de erro

# Verificar se uma chave existe:
# if capitals.get("Russia"):
#     print("Capital registrada")
# else:
#     print("Capital não encontrada")

# Modificações comuns:
# capitals.update({"Germany": "Berlin"})   # adiciona/atualiza
# capitals.update({"USA": "Detroit"})      # sobrescreve valor
# capitals.pop("China")                    # remove chave específica
# capitals.popitem()                       # remove último item
# capitals.clear()                         # esvazia o dicionário

# Iterar apenas pelas chaves:
# for key in capitals.keys():
#     print(key)

# Iterar apenas pelos valores:
# for value in capitals.values():
#     print(value)

# Iterar por chave e valor:
for key, value in capitals.items():
    print(f"{key}: {value}")
