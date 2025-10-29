"""
Exercicio

exiba os índices da lista
0 Maria
1 Helena
2 Luis
"""
lista = ['Maria', 'Helena', 'Luis']
lista.append(4)
indices = range(len(lista))


for i in indices:
    print(i, lista[i], type(lista[i]))