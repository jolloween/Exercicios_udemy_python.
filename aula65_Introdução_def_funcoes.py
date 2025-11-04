"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmentro (argumentos)
e retormar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
# def Print():
#     print('várias4')
#     print('várias3')
#     print('várias2')
#     print('várias1')

# Print()

# def imprimir(a, b, c): #abc são parâmetros
#     print(a, b, c)

# imprimir(1, 2, 3)# 123 são argumentos
# imprimir(4, 5, 6)#também são argumentos

def saudacao(nome='sem nome'): # como não ter argumento na linha 30. nome='sem nome' 
    print(f'olá, {nome}!')


saudacao('João Paulo')
saudacao('Maria')
saudacao('Fátima')
saudacao()



