"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 #variável global

def scopo(): #escopo local
    global x
    x = 10 # variável local do escopo externo linha 12,20
    def outra_funcao():
        global x
        x = 11
        y = 2 #variável local do escopo interno linha 14, 17
        print(x, y)

    outra_funcao()#escopo interno
    print(x) #escopo externo

print(x) #global
scopo() # vai imprimir o escopo local quando for chamado a função
print(x)#global