preco_unitario = float(input("digite o preço unitario do produto"))
quantidade = int(input("Digite a quantidade comprada: "))
total = preco_unitario * quantidade

if quantidade > 10:
    total *=0.9

    print(f"o valor total da compra é: R$ {total:.2f}")