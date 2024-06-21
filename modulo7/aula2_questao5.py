import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    resultado = []

    for palavra in palavras:
        if len(palavra) > 3:
            inicio = palavra[0]
            fim = palavra[-1]
            letras_internas = list(palavra[1:-1])
            random.shuffle(letras_internas)
            palavra_embaralhada = ''.join([inicio] + letras_internas + [fim])
            resultado.append(palavra_embaralhada)
        else:
            resultado.append(palavra)

    return ' '.join(resultado)

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
