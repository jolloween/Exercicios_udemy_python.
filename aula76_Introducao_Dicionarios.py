# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'João Paulo',
#     'sobrenome': 'Pedrosa Soares',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='João Paulo', sobrenome='Pedrosa')

# dados = {}
# dados['nome'] = 'João'
# dados['sobrenome'] = 'Pedrosa'
# dados['nome'] = 'fatima' #alterar
# print(dados)
# # print(dados['nome'])

# for chave, valor in dados.items():
#     print(f'{chave}: {valor}')

pessoa = {
    'nome': 'João Paulo',
    'sobrenome': 'Pedrosa Soares',
    'altura': 1.80,
    'peso': 76.00,
    'endereco': [{'rua:': 'boa nova',
                'numero:': 118, 'andar:': 'seg esq trs'},
                {'rua:': 'Av jose Francisco dos santos',
                'numero:': 436}]
}

# print(pessoa, type(pessoa))
# endereco = pessoa['endereco'][1]
# print('Rua:', endereco['rua:'])
# print('numero', endereco['numero:'])

# print(pessoa['nome'])
# print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])


