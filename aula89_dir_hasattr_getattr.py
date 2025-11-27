# dir, hasattr e getattr em python

string = 'João'
metodo = 'upper'
if hasattr(string, 'upper'):
    print('existe upper')
    print(string.upper())


if hasattr(string, metodo):
    print('existe upper')
    print(getattr(string, metodo)())
else:
    print('não existe o método', metodo)