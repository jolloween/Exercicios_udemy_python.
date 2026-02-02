import importlib
import aula98m

#limpar_tela()

# print(variavel)

# for i in range(10):
#     aula98m.variavel # Não irá repetir por se tratar de um singleton
#     print(i)

# print('Fim.')


print(aula98m.variavel)

for i in range(10):
    importlib.reload(aula98m)
    print(i)
print('fim')















