matriz = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]



#iterar sobre cada linha da matriz
for linha in matriz:
    #iterar sobre cada elemento da linha
    for elemento in linha:
         print(elemento, end=' ')
    #imprimir uma linha após cada linha matriz
    print()

    