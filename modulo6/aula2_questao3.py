import random
from collections import Counter

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = list(set(lista1) & set(lista2))
interseccao.sort()

contagem1 = Counter(lista1)
contagem2 = Counter(lista2)

print("lista1:", lista1)
print("lista2:", lista2)
print("Interseccao:", interseccao)

print("Contagem:")
for num in interseccao:
    print(f"{num}: (Lista 1 = {contagem1[num]}, Lista 2 = {contagem2[num]})")
