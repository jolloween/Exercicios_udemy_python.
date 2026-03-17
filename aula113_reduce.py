#TODO:  reduce - faz a redução de um iterável em um valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)
print('total é', total )
#######################################
# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']

# total = reduce(
#     funcao_do_reduce,
#     produtos,
#     0
# )
########################################
# print('total é', total )
# # Total forma tradicional
# soma = 0
# for produto in produtos:
#     soma += produto['preco']
# print(f'{soma:.2f}€')

# #total com list comprehension
# total = sum([p['preco'] for p in produtos])
# print(f'{total:.2f}£')