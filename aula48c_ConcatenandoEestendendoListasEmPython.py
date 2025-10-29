"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
create read update   delete
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
criar, ler, alterar, apagar = lista[i] (CRUD)

"""
lista_a = [1, 2, 3 ]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b #junção da lista_A com a lista_b
print(lista_c)
lista_a.extend(lista_b) # a lista foi incluída na lista_a
print(lista_a)