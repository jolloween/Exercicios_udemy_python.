#Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
print(not True)  # False
print(not False)  # True

# UMA STRING VAZIA É AVALIADA COMO FALSO.
senha = input('Senha: ')
if not senha: 
    print('Você digitou nada.')