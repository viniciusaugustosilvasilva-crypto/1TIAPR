# Cria duas matrizes 3x3
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Soma das matrizes
soma = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz1[i][j] + matriz2[i][j])
    soma.append(linha)

# Exibe o resultado
print("Matriz 1:")
for linha in matriz1:
    print(linha)

print("\nMatriz 2:")
for linha in matriz2:
    print(linha)

print("\nSoma das matrizes:")
for linha in soma:
    print(linha)
    