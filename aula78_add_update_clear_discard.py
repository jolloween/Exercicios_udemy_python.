# Métodos úteis:
add, update, clear, discard
s1 = set()
s1.add(1)
s1.add('João') #Adiciona algo dentro do set
s1.update(('Bom dia', 2, 3))
#s1.clear() limpa tudo que tá dentro do set
s1.discard('João') # posso definir o que descartar dentro do meu set
print(s1)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 #Union - faz junção dos conteúdos sem repetir
s3 = s1 & s2 # intersecção - me mostra os intens repetidos
s3 = s1 - s2 #Itens presentes apenas no set da esquerda
s3 = s1 ^ s2 #Itens que não estão prensetes em ambos
print(s3)