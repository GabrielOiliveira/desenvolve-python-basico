import itertools

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

anagramas = [palavra for palavra in frase.split() if sorted(palavra.lower()) == sorted(palavra_objetivo.lower())]

print(f"Anagramas: {anagramas}")
