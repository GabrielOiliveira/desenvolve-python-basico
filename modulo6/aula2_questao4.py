quantidade_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
for i in range(quantidade_lista1):
    lista1.append(int(input(f"Digite o elemento {i+1} da lista 1: ")))

quantidade_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
for i in range(quantidade_lista2):
    lista2.append(int(input(f"Digite o elemento {i+1} da lista 2: ")))

lista_intercalada = []
i, j = 0, 0
while i < len(lista1) and j < len(lista2):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[j])
    i += 1
    j += 1

lista_intercalada.extend(lista1[i:])
lista_intercalada.extend(lista2[j:])

print("Lista Intercalada:", " ".join(map(str, lista_intercalada)))