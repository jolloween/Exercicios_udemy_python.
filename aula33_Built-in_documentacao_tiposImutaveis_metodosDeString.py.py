"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'joão Paulo'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
print(string.capitalize()) #esa função tranasforma a primeira letra em maiscula.

string = '1000'
print(string.zfill(10)) #vai por 10 zeros a esquerda