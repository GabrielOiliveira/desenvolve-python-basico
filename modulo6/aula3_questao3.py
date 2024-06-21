import random

lista = [random.randint(-10, 10) for _ in range(20)]

print("Original:", lista)

inicio_maior_intervalo = 0
tamanho_maior_intervalo = 0
inicio_atual = None
contador_negativos = 0

for i, num in enumerate(lista):
    if num < 0:
        if inicio_atual is None:
            inicio_atual = i
        contador_negativos += 1
    else:
        if contador_negativos > tamanho_maior_intervalo:
            inicio_maior_intervalo = inicio_atual
            tamanho_maior_intervalo = contador_negativos
        inicio_atual = None
        contador_negativos = 0

if contador_negativos > tamanho_maior_intervalo:
    inicio_maior_intervalo = inicio_atual
    tamanho_maior_intervalo = contador_negativos

if tamanho_maior_intervalo > 0:
    del lista[inicio_maior_intervalo:inicio_maior_intervalo + tamanho_maior_intervalo]

print("Editada:", lista)
