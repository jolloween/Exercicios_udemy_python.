# TODO: combinations, permutations e product - itertools
#Combinação - ordem  não importa - iteravel + tamanho do grupo
# Pemutação - ordem não importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['Masculino', 'Feminino', 'Unisex'],
    ['Algodão', 'poliéster'],
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
