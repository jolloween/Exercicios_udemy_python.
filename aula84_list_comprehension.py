# 137. Introdução à List comprehension em Python
# é uma forma rápida de criar listas a partir de iteráveis.

# print(list(range(10)))

# list = []

# for numero in range(0,10):
#     list.append(numero)

# list = [numero  for numero in range(10+1)]
# print(list)

# list = [
#     numero * 2 #é possível multiplicar.
#     for numero in range(10)]
# print(list)

#mapeamento de dados em list comphension
import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produtos = [
        {'nome': 'p1', 'preco': 20,},
        {'nome': 'p2', 'preco': 10,},
        {'nome': 'p3', 'preco': 30,},
]


# novo_produto = [
#             produto #é possivel especificar, ou seja. produto['nome'] ou produto['preco']
#             for produto in produtos
# ]

# novo_produto = [
#                 {'nome': produto['nome'], }
#                 for produto in produtos
# ]

novo_produto = [
                {**produto, 'preco': produto['preco'] * 1.05  }
                if produto['preco'] > 20 else {**produto}
                for produto in produtos
]


# print(novo_produto)
# print(*novo_produto, sep="\n")
#p(novo_produto) #chamei a funcao para ser feito o pprint

#FILTRAR LISTA

lista = [n for n in range(10) if n < 5] # usamos o if apos o for.
print(lista)

novo_produto = [
                {**produto, 'preco': produto['preco'] * 1.05  }
                if produto['preco'] > 20 else {**produto} #para ser feito o mapeamennto tem que ser antes do for
                for produto in produtos
                if produto['preco'] > 10 #para filtar o  if tem que ser após o for
]
p(novo_produto)

