"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1]) #tb é possível escolhar um ítem da tupla.
print(nomes)
print('-=' * 20)
nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)# é possível converter uma lista para uma tuple
print(nomes)
print('-=' * 20)


#também é possível converter uma tupla em uma lista.
nomes =['Maria', 'Helena', 'Luiz']
nomes = list(nomes)# é possível converter uma lista para uma tuple
print(nomes)