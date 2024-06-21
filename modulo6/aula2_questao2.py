import random

num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

soma = sum(elementos)
media = soma / num_elementos

print("Lista de Elementos:", elementos)
print("Soma dos Valores:", soma)
print("Média dos Valores:", media)
