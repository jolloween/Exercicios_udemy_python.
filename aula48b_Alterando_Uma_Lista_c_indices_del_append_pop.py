"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
create read update   delete
criar, ler, alterar, apagar = lista[i] (CRUD)

"""

lista = [10, 20, 30, 40]
# numero = lista[2] # posso atribuir um item da lista em uma variável
# print(numero) # 30

# lista[-2] = 300 # é possível alterar algo na lista
# print(lista)

# del lista[1] # é possível alterar um índice da lista com a função del
# print(lista)
lista.append(300) # Adiciona um valor no final da lista.
lista.pop() # Remove o último item da lista.
lista.append(400) # Adiciona um valor no final da lista.
lista.append(500) # Adiciona um valor no final da lista.
lista.append('maria') # Adiciona um valor no final da lista.
ultimo_valor = lista.pop() # foi atribuido a variável o ultimo item removido com a funcão pop
# ultimo_valor = lista.pop(3) # tabém pode ser removido um item através de índice com a função pop
print(lista, 'Removido,', ultimo_valor)
print(lista)
