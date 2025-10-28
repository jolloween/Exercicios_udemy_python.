""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break #encontrou espaço na string e o else não foi executado.

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')

""""Segundo exemplo"""


string = 'Valorqualquer' #sem espaços

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break #como não tem espaços na vvariavels string o else foi executado.

    print(letra)
    i += 1
else:
    print('encontrei um espaço na string.')
print('Fora do while.')
