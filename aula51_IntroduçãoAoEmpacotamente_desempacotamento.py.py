"""
Introdução ao empacotamento e desempacotamento
"""
# _, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
# print(nome)

nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes #é possível atribuir variaveis com desempacotamento
                            #através da lista.
#OU
nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']

print(nome1) #Maria
print(nome2) #Helena
print(nome3) #Luiz
print('-=' * 20)
nome1, *_ = ['Maria', 'Helena', 'Luiz'] # é possível atribuir um valor a variável,
                                            # e por o restante em uma lista
print(nome1)                                 
print(_)

print('-=' * 20)
#caso queira pegar o segundo nome segue exemplo abaixo:
_, nome2, *_ = ['Maria', 'Helena', 'Luiz'] 
print(nome2)


