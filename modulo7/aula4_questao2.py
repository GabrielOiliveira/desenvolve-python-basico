import os

caminho_frase = os.path.join(os.getcwd(), "frase.txt")
caminho_palavras = os.path.join(os.getcwd(), "palavras.txt")

with open(caminho_frase, 'r') as arquivo_frase:
    conteudo = arquivo_frase.read()

palavras = []
for palavra in conteudo.split():
    palavra_limpa = ''.join(caracter for caracter in palavra if caracter.isalpha())
    if palavra_limpa: 
        palavras.append(palavra_limpa.lower())

with open(caminho_palavras, 'w') as arquivo_palavras:
    for palavra in palavras:
        arquivo_palavras.write(palavra + '\n')

print(f"Conteúdo do arquivo {caminho_palavras}:")
with open(caminho_palavras, 'r') as arquivo_palavras:
    conteudo_palavras = arquivo_palavras.read()
    print(conteudo_palavras)
