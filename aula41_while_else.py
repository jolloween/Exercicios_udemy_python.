""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break #encnotrou espaç na string e o else não executado.

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')