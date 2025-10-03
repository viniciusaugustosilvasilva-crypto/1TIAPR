# Crie sua matriz 3x3 aqui para testar
matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
 
# Vamos assumir que a matriz é identidade até que se prove o contrário
eh_identidade = True
 
# Laço para percorrer as linhas (índice i)
for i in range(3):
    # Laço para percorrer as colunas (índice j)
    for j in range(3):
        # 1. Se o elemento está na diagonal principal (i == j), ele deve ser 1.
        if i == j and matriz[i][j] != 1:
            eh_identidade = False
            break  # Se a regra for quebrada, não precisa mais checar
 
        # 2. Se o elemento está fora da diagonal principal (i != j), ele deve ser 0.
        if i != j and matriz[i][j] != 0:
            eh_identidade = False
            break  # Se a regra for quebrada, não precisa mais checar
   
    # Se já descobrimos que não é identidade, podemos parar o laço externo também
    if not eh_identidade:
        break
 
# Imprime o resultado final
if eh_identidade:
    print("A matriz É uma matriz identidade.")
else:
    print("A matriz NÃO é uma matriz identidade.")