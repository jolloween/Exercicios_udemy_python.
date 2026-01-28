# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return
# exemplo 1
# gen = generator()
# for n in gen:
#     print(n)
#exemplo 2
# gen = generator(n=5, maximum=8) #posso fazer um range
# for n in gen:
#     print(n)
#exemplo 3
gen = generator(maximum=1000000)
for n in gen:
    print(n)

    
#######################################################
# def generator(n=0):
#     yield 1 # Pausar
#     print('Continuando...')
#     yield 2 # Pausar
#     print('mais uma vez...')
#     yield 3 # Pausar
#     print('VOu terminar.')
#     return 'ACABOU'


gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# agora com o for:

# for n in gen:
#     print(n)