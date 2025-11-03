#Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['maria', 'Helena', 1, 2 , 3, 'Eduarda']
tupla = 'python', 'é', 'legal'

# p, b, *_, ap, u = lista
# print(p, b, ap, u)

# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]


print(*lista)
print(*salas, sep='\n')