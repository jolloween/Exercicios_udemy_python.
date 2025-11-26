# 137. Introdução à List comprehension em Python
# é uma forma rápida de criar listas a partir de iteráveis.

# print(list(range(10)))

# list = []

# for numero in range(0,10):
#     list.append(numero)

list = [numero  for numero in range(10+1)]
print(list)

list = [
    numero * 2 #é possível multiplicar.
    for numero in range(10)]
print(list)

