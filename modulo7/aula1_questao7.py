import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []

    for nome in nomes:
        nome_criptografado = ''.join(chr(ord(letra) + chave) for letra in nome)
        nomes_criptografados.append(nome_criptografado)

    return nomes_criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

print(f"Chave aleatória: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_cript}")
