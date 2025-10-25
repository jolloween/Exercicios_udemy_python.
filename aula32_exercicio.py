"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')

if entrada.isdigit():
    par_impar = int(entrada)
    if par_impar % 2 == 0:
        print(f'{par_impar} é par.') 
    else:
        print(f'{par_impar} é ímpar.')    
else:
    print('Você não digitou um número inteiro.') 

# TODO OUTRO EXEMPLO
entrada = input('Digite um número: ')      

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar is True:
        par_impar_texto = 'Par'
    print(f'o númmero {entrada} é {par_impar_texto}')
else: 
    print('Você não digitou um número inteiro.')

# TODO OUTRO EXEMPLO 2
entrada = input('Digite um número: ')      

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar is True:
        par_impar_texto = 'Par'
    print(f'o númmero {entrada} é {par_impar_texto}')
except: 
    print('Você não digitou um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input('Qual horas são agora (0-23)'))
if 0 <= hora <= 11:
    print('Bom dia!')
elif 12 <= hora <= 17:
    print('Boa tarde!')
else:
    print('boa noite!')    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". """

nome = input('Qual seu nome: ')
tamanho_nome = len(nome)
print(tamanho_nome)
if tamanho_nome <= 4:
    print(f'seu nome {nome} é curto.')
elif  4 < tamanho_nome <= 6:
    print(f'Seu nome {nome} é normal.')    
else:
    print(f'Seu nome {nome} é muito grande.')    
