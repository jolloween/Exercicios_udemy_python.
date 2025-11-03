"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip - corta os espaços
"""
# frase = '      Olha só que   ,   coisa interessante      '
# lista_frases = frase.split(', ')

# for i, frase in enumerate(lista_frases):
#     print(lista_frases[i].strip())

# print(lista_frases)

# #Corrigindo os epaços da lista com strip()

# for i, frase in enumerate(lista_frases):
#     lista_frases[i] = lista_frases[i].strip()

# print(lista_frases)    

# nova lista 

frase = '      Olha só que   ,   coisa interessante      '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(listas_frases)
frases_unidas = ', '.join('lista_frase')
print(frases_unidas)