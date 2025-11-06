# p1 = {
#     #'nome': 'João Paulo',
#     'sobrenome': 'Pedrosa Soares'}

# print(p1.get('nome', None))# me retrona None caso a chave não exista

# p2 = {
#     'nome': 'João Paulo',
#     'sobrenome': 'Pedrosa Soares'
# }
# nome = p2.pop('nome')
# print(nome)#mostra o valor do nome
# print(p2)#remove a chave nome e valor.

# p3 = {
#     'nome': 'João Paulo',
#     'sobrenome': 'Pedrosa Soares'
# }

# ultima_chave = p3.popitem() # remove a ultima chave
# print(ultima_chave)#mostra a chave removida
# print(p3)#o restante do dicionário

p3 = {
    'nome': 'João Paulo',
    'sobrenome': 'Pedrosa Soares'
}

p3.update({'nome': 'Fátima',
        'idade': 'forever yong'}) #atualiza a lista com uma chave existente ou criar uma nova.
print(p3)

p3.update(altura=1.80, peso=76.30)#também pode atualizar o dicionário usando argumentos
print(p3)

# lista = [['nome', 'Felipe'], ['idade', 39]]
# p3.update(lista)
# print(p3)
