# ENUMERATE - enumera iteráveis (índices)



listas = ['Maria', 'Helena', 'Luiz']
listas.append('João')
lista_lista_enumerada = list(enumerate(listas)) # vai enumerar os itens dentro de uma lista
print(lista_lista_enumerada)




for item in enumerate(listas): # vai iterar meus intens da listas.
    print(item)

print('-=' * 20)

for indice, nome in enumerate(listas): # mais aconselhável de usar
    print(indice, nome)

print('-=' * 20)

for tupla_enumerada in enumerate(listas):
    print('For da tupla')
    for valor in tupla_enumerada:
        print(f'\t{valor}')




