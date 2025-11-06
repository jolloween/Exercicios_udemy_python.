# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {'nome': 'João Paulo', 'Sobrenome': 'Pedrosa Soares'}
print(len(pessoa)) #quantidades de chaves
print(pessoa.keys())#mostra as chaves do dicionário
print(pessoa.values())#mostra os valores do dicionário
print(pessoa.items())#mostra a chave e valor
pessoa.setdefault('idade', None)#usamos oo setdefault quando não tivermos a chave
print(pessoa['idade'])

for chave, valor in pessoa.items(): #parecido com o enumerate, pois é utilizado em dicionário
    print(chave, valor)
