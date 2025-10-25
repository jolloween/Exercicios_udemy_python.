primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor} é maior que "
          f"{segundo_valor}")
elif primeiro_valor == segundo_valor:
    print("Os valores digitados são iguais.")    
else:
    print(f"{segundo_valor} é maior que"
          f" {primeiro_valor}")