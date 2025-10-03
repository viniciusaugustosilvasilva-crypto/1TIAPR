# Criando uma matriz 3x2
matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]
 
print("Matriz original (3x2):")
for linha in matriz:
    print(linha)
 
# Calculando a transposta manualmente
transposta = []
for j in range(len(matriz[0])):  # número de colunas da matriz original
    nova_linha = []
    for i in range(len(matriz)):  # número de linhas da matriz original
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)
 
print("\nMatriz transposta (2x3):")
for linha in transposta:
    print(linha)