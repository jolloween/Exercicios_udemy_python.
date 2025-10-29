"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
print("=-"*20)
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() #foi feito uma cópia da lista_a. neste caso a variável_b fica imutável.
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)