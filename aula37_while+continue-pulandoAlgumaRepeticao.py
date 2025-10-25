contador = 0

while contador < 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6')
        continue

    if 10 <= contador <= 27:
        print('não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break
    
print('acabou!')    
