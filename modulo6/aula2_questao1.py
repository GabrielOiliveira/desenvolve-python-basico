import random

valores = [random.randint(-100, 100) for _ in range(20)]

ordenada = sorted(valores)

print("Lista Original:", valores)

indice_maior = valores.index(max(valores))

indice_menor = valores.index(min(valores))

print("Lista Ordenada:", ordenada)
print("Índice do Maior Valor:", indice_maior)
print("Índice do Menor Valor:", indice_menor)