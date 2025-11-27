produto = {
        'nome': 'caneta azul',
        'preco': 2.5,
        'categoria': 'escritorio',
}

dic = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    # if chave != 'categoria' é possível especificar qual item será alterado
}


lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor a'),
]

print(dict(lista)) #converte meu dicionário e em lista
# dc = {
#     valor: chave
#     for valor, chave in lista
# }

#set comprehension
s1 = {i for i in range(10)}
