"""
EXERCICIOS
1 - Soma simples
Crie uma função soma(a, b) que receba dois números e retorne a soma deles.
"""

def soma(a, b):
    print(a+b)

soma(1, 3)

"""
2 - Mensagem personalizada
Crie uma função saudacao(nome) que receba um nome e imprima:
"Olá, [nome]! Seja bem-vindo!".
"""

def saudacao(nome):
    print(f'Olá, {nome}, Seja bem vindo!')

saudacao('João Paulo')

"""
3 - Dobro de um número
Escreva uma função dobro(x) que receba um número e retorne o dobro dele.
"""
def dobro(x):
    print(f'O dobro de {x} é:' , x**2)

dobro(2)

"""
4- Número par ou ímpar
Crie uma função par_ou_impar(n) que receba um número e retorne 
"Par" se for par ou "Ímpar" se for ímpar.
"""
# def par_impar(n):
#     if n % 2 == 0:
#         print(f"O número {n} é par.")
#     else:
#         print(f"o número {n} é impar.")

# numero = int(input("Digite um número:"))
# par_impar(numero)

"""
5 - Maior número
Crie uma função maior(a, b) que receba dois números e retorne o maior deles.
"""

# def maior(x, y):
#     if x > y:
#         print(f'o número {x} é maior que {y}')
#     else:
#         print(f'o número {y} é maior que {x}')
# numero1 = int(input("Digite um número: "))
# numero2 = int(input('Digite outro número'))

# maior(numero1, numero2)

"""
6 - Área do retângulo
Faça uma função area_retangulo(largura, altura) que retorne a área (base × altura).
"""
# def area_retangulo(largura, altura):
#     area = largura * altura
#     return area #retorna para a variável resultado.

# larg = float(input('Digite a largura do retangulo (m): '))
# alt = float(input('Digite a altura do retangulo (m): '))
# resultado = area_retangulo(larg, alt)
# print(f'a área do retangulo é {resultado}m²')

"""
7 - Média de três notas
Escreva uma função media(n1, n2, n3) que calcule e retorne a média das três notas.
"""
# def media(n1, n2, n3):
#     nota = (n1 + n2 + n3) / 3
#     return nota


# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))


# resultado = media(nota1,nota2, nota3)
# print(f'A média foi: {resultado}')

"""
8 - Conversor de temperatura
Crie uma função celsius_para_fahrenheit(c) que converta °C para °F usando a fórmula:
f = c x 1.8+32
"""
# def celsius_para_fahrenheit(c):
#     conversor = (c * 1.8) + 32
#     return conversor

# celsius = float(input("Digite a temperatura em celcius: "))
# resultado = celsius_para_fahrenheit(celsius)
# print(f'a tempera em celsius {celsius} convertido para fahrenheit é {resultado}°F ')

"""
9 - Contagem regressiva
Crie uma função contagem_regressiva(n) que imprima uma contagem de n até 0 e depois escreva "Fim!".
"""
# import time
# def contagem_regressiva(n):
#     while n >= 0:
#         print(n)
#         time.sleep(1)
#         n -= 1
# n = int(input("Digite um número para iniciar a contagem regressiva: "))
# contagem_regressiva(n)
# print('fim')
"""
10 - Verificador de palíndromo
Escreva uma função eh_palindromo(palavra) que retorne True se a
palavra for igual quando lida de trás para frente (ex: "arara", "radar").
"""
def eh_palindromo(palavra):
    # Remove espaços e coloca tudo em minúsculas para evitar erros
    palavra = palavra.replace(" ", "").lower()
    
    # Verifica se a palavra é igual ao seu inverso
    if palavra == palavra[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo!")

# --- programa principal ---
texto = input("Digite uma palavra ou frase: ")
eh_palindromo(texto)