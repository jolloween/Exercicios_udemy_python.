"""
Listas dentro de listas

"""
salas = [
    # 0         1
    ['Maria', 'Helena', ], #0
    # 0
    ['Helaine', ],  #1
    # 0        1      2
    ['Luiz', 'João', 'Eduarda',], # 2
]

# print(salas[1][0]) #Helaine
# print(salas[0][1]) #Helena
# print(salas[2][1]) #João
# print(salas[2][2]) #Eduarda
# print(salas[2][3][2]) #20

for sala in salas:
    print(f'a sala é: {sala}')
    for aluno in sala:
        print(aluno)
