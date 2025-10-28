while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Qual operador você quer (+-*/): ')

    numeros_validos = True

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
    except ValueError:
        numeros_validos = False

    if not numeros_validos:
        print("Um ou ambos os números digitados são inválidos.")
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print("Digite um operador válido.")
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} =', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} =', numero_1_float - numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float} =', numero_1_float * numero_2_float)
    elif operador == '/':
        if numero_2_float == 0:
            print("Erro: não é possível dividir por zero.")
            continue
        print(f'{numero_1_float} / {numero_2_float} =', numero_1_float / numero_2_float)

    sair = input("Quer [S]air: ").lower().startswith('s')
    if sair:
        break