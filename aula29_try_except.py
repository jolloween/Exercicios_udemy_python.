"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input("Vou dobrar o número que você digitar: ")

try:
    print(f'str: , {numero_str} ')
    numero_float = float(numero_str)
    print(numero_float)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except numero_str as e:
    print(f"Isso não é um número.{e}")    

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(numero_float)
#     print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número.')    
