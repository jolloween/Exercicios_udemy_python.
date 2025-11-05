#exercícios com funções

#crie uma função que multiplica todos os argumentos
#não nomeados recebidos
#Retorne o total para uma variável e mostre o valor da variável.

# def multiplica(*args):
#     total = 1
    
#     for numero in args:
#         total *= numero
#     return total 
# resultado = multiplica(2,4,6,8)
# print(resultado)

# Crie uma função que retorne se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# def par_ou_impar(number):
#     if number % 2 == 0:
#         par = 'é PAR'
#         return par
#     return 'é ÍMPAR'
        
        
# #programa principal
# numero = int(input('Digite um número: '))
# resultado = par_ou_impar(numero)
# print(f'O número {numero} {resultado}')


def par_impar(numero):
    multiplo_de_2 = numero % 2 == 0
    if multiplo_de_2:
        return f'{numero} é par'
    return f'{numero} é ímpar'
print(par_impar(2))
print(par_impar(4))
print(par_impar(5))
print(par_impar(7))
print(par_impar(8))

