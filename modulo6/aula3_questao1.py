print("Digite pelo menos 4 números inteiros (digite 'fim' para parar):")
numeros = []
while True:
    entrada = input("Digite um número inteiro ou 'fim' para parar: ")
    if entrada.lower() == 'fim':
        break
    numeros.append(int(entrada))

if len(numeros) < 4:
    print("É necessário digitar pelo menos 4 números inteiros.")
else:
    print("Lista Original:", numeros)
    print("Os 3 primeiros elementos:", numeros[:3])
    print("Os 2 últimos elementos:", numeros[-2:])
    print("Lista Invertida:", numeros[::-1])
    print("Elementos de índice par:", numeros[::2])
    print("Elementos de índice ímpar:", numeros[1::2])
