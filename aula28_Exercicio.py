"""
Formatação básica de strings
s - string
"""
"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Qual seu nome? ")
idade = input('Qual a sua idade? ')
if nome and idade: #string vazia é confrotado com bool. Então é False.
    print(f"Seu nome é {nome} ")
    print(nome[: : -1]) # vai ler o nome de trás para frente
    if " " in nome:
        print(f"seu nome {nome} contém espaço.")
    else:
        print("Seu nome não contém espaços.")    
    print(f'Seu nome tem {len(nome)} letras.') 
    print(f"A primeira letra do seu nome é {nome[0]}")   
    print(f"A última letra de seu nome é {nome[-1]}")
else:
    print('Desculpe, você deixou campos vazios.')    
 
