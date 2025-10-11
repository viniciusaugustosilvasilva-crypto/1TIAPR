def soma(a, b):
    return a + b    

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b    

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return a / b 
    
    resultado_soma = soma(10, 5)
    print(f"Soma: {resultado_soma}")

    resultado_subtracao = subtrai(10, 5)
    print(f"Subtração: {resultado_subtracao}")

    resultado_multiplicacao = multiplica(10, 5)
    print(f"Multiplicação: {resultado_multiplicacao}")

    resultado_divisao = divide(10, 5)
    print(f"Divisão: {resultado_divisao}")      print("Erro: Divisão por zero não é permitida.")