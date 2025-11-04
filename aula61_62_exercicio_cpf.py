"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '529.982.247-25'
novo_cpf = cpf \
    .replace('.', '') \
    .replace('-', '') # '.' e ',' serão substituido por uma ""

nove_digitos = novo_cpf[:9] #fatiamento(será mostrado os 9 primeiros digitos)
dez_digitos = novo_cpf[:10] #Fatiamento(será mostrados os 10 primieros números sequenciais.)

# Validação do primeiro digito

contagem_regressiva1 = 10 #contador
mult_soma = 0

for digito in nove_digitos:
    mult_soma += (int(digito) * contagem_regressiva1)
    
    contagem_regressiva1 -= 1

print("-=" *20)    
print(f'a multiplicação e a soma do'
    f'primeiro dígito foi: {mult_soma}')
resto_div = (mult_soma * 10) % 11
print("-=" *20)   
print(f'o resto da divisão do primeiro digito foi: {resto_div}')
#------------------------------------------------------
# Validação do segundo digito

contagem_regressiva2 = 11
mult_soma2 = 0

for SegDigito in dez_digitos:
    mult_soma2 += int(SegDigito) * contagem_regressiva2
    
    contagem_regressiva2 -= 1

print("-=" *20)
print(f'a multiplicação e a soma do'
    f'segundo digito foi: {mult_soma2}')# multiplicação dos numeros e a soma entre eles
resto_div2 = (mult_soma2 * 10) % 11
print("-=" *20)
print(f'O resdo da divisão do segundo dígito foi: {resto_div2}')

#validação do CPF primeiro dígito
if resto_div == int(novo_cpf[9]):
    print("-=" *20)
    print('primeira verificação válida')
    print('o resto da divisão é igual ao primeiro dígito do CPF')
    print("-=" *20)
else:
    print('Validação do primeiro dígito inválida.')

#validação do CPF segundo dígito
if resto_div2 == int(novo_cpf[10]):
    print("-=" *20)
    print('segunda verificação válida')
    print('o resto da divisão é igual ao segundo dígito do CPF')
    print("-=" *20)

else:
    print('validação do segundo dígito inválida')










