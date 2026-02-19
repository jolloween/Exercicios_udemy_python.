#TODO: Somando duas listas.

"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:"""

from itertools import zip_longest
l1= [1, 2, 3, 4, 5, 6, 7]
l2= [1, 2, 3, 4]
lenght = len(l2)
# lista_c = lista_a + lista_b
lista_soma = []

print(list(zip(l1, l2))) #União das duas listas usando o zip

#1º forma:
for i in range(len(l2)):
    lista_soma.append(l1[i] + l2[i])
print(lista_soma)

#2º forma:

for i, _ in enumerate(l2):
    lista_soma.append(l1[i] + l2[i])
print(lista_soma)

#3º forma:
lista_zip = [x + y for x, y in zip(l1, l2)]
print(lista_zip)

lista_zip_longest = [x + y for x, y in zip_longest(l1, l2, fillvalue=0)] #mantém os valores da outra lista 
print(lista_zip_longest)