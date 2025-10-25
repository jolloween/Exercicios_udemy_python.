# \r\n -> CRLF
# \n -> LF
"""
comando end="\n" posso fazer uma quebra de linha. ou juntar a outra
linha com apenas end=""
"""
print(12, 34, 1011, sep='-', end="##") # sep permite por algo entre os espaços
print(56, 78, sep="-", end="\n")
print(98, 10, sep="-", end="\n")

