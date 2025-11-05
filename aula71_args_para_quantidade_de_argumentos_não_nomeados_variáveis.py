"""
args - Argumentos não nomeados
* - *args (empacontamento e desempacotamento)
"""
#Lembre-te de desempacotamento

# x, y, *resto = 1,2,3,4
# print(x,y, resto)

# def soma(*args):
#     #args =list(args) convertendo para uma lista
#     somatotal = sum(*args) # desempacotamento
#     return somatotal

# resultado = soma((1,2,3,4,5,6))
# print(resultado)

# def soma(*args):
#     somatotal = 0 # acumulador dos números
#     for numero in args:
#         somatotal += numero #soma de todos os números
#     print(f'A soma total foi: {somatotal}')
# soma(1,2,3,4,5,6)

def soma(*args): #argumetos não nomeados. args empacota e o * desempacota
    somatotal = 0 # acumulador dos números
    for numero in args:
        somatotal += numero #soma de todos os números
    return somatotal #retorna para o programa principal
#programa princiapal
resultado = soma(1,2,3,4,5,6)
print(f'A soma total dos números foi: {resultado}')

resultado2 = soma(5,6,4,2,1,3,4)
print(f'A soma total dos números foi: {resultado2}')

resultado3 = soma(9,8,7,4,5,6,3,2,1)
print(f'A soma total dos números foi: {resultado3}')