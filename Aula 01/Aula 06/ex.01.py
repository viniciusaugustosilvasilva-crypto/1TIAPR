arquivo = "texto.txt"

with open(arquivo, "r", encoding="utf-8") as f:
    conteudo = f.read()
    palavras = conteudo.split()
    num_palavras = len(palavras)
    
    print(f"Número de palavras: {num_palavras}")