letras = set()

while True:
    letra = input("Digite uma letra:")
    letras.add(letra.lower())

    if "l" in letra:
        print("Parabéns, você encontrou a letra misteriosa.")
        break
print(letras)
