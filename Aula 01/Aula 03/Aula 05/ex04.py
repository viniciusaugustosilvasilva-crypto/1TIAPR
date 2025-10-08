def conta_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for char in texto if char in vogais)