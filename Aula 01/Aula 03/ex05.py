# Matriz A (2x3: 2 linhas, 3 colunas)
matriz_A = [
    [1, 2, 3],
    [4, 5, 6]
]
 
# Matriz B (3x2: 3 linhas, 2 colunas)
matriz_B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
 
# A matriz resultante será 2x2, vamos inicializá-la com zeros
resultado = [
    [0, 0],
    [0, 0]
]
 
# --- Cálculo da Multiplicação ---
 
# Laço para percorrer as linhas da matriz_A (e do resultado)
for i in range(len(matriz_A)):
    # Laço para percorrer as colunas da matriz_B (e do resultado)
    for j in range(len(matriz_B[0])):
        # Laço para calcular o produto escalar (percorre colunas de A e linhas de B)
        soma = 0
        for k in range(len(matriz_B)):
            soma += matriz_A[i][k] * matriz_B[k][j]
       
        # Armazena a soma na posição correta da matriz resultado
        resultado[i][j] = soma
 
# --- Imprimir o resultado ---
print("Matriz A (2x3):")
for linha in matriz_A:
    print(linha)
 
print("\nMatriz B (3x2):")
for linha in matriz_B:
    print(linha)
 
print("\nResultado da Multiplicação (2x2):")
for linha in resultado:
    print(linha)
 