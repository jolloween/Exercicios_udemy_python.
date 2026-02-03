#copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)



import copy

from dados import produtos

# novos_produtos = [
#     {**p, 'preco': round(p['preco'] *1.10, 2)}
#     for p in copy.deepcopy(produtos)
# ]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},

# ]

novos_produtos = copy.deepcopy(produtos)

#aumenta em 10% e ordenado por nome em ordem decrescente
novos_produtos.sort(key=lambda p: p['nome'], reverse=True)
for p in novos_produtos:
    p['preco'] = round(p['preco'] * 1.10, 2)


print("Podutos com preço antigo")
print(*produtos, sep='\n')
print()
print("Preço atualizado em 10%")
print(*novos_produtos, sep='\n')