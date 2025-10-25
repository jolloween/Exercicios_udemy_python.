"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
# variavel = 'Olá mundo'
# print(f'{variavel[4:8]}') #começa do m e vai até o d 
# print(f'{variavel[::-1]}') # vai ler de trás para frente de um e um. do final até o ínicio
# print(f'{variavel[4:]}') # vai do m até o final
# print(f'{variavel[:5]}') # vai do ínicio até o m
# print(f'{variavel[-8:-2]}') # começa do l até n
# print(f'{variavel[3]}') # vai contar o espaço pq também é um caractere
# print(len(variavel)) # a função len vai me mostrar a quantidade de caractere
variavel = 'Olá mundo'
print(f'{variavel[0 : len(variavel) : 2]}') # vai ser feito a contagem de 2 em dois
print(f'{variavel[0 : 9 : 2]}') # mesma coisa que o exemplo acima.