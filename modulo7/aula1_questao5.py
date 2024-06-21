frase = input("Digite uma frase: ")

vogais = [letra for indice, letra in enumerate(frase) if letra.lower() in 'aeiou']
indices_vogais = [indice for indice, letra in enumerate(frase) if letra.lower() in 'aeiou']

print(f"{len(vogais)} vogais")
print(f"Índices {indices_vogais}")
