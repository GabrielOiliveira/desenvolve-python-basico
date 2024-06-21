import random
import math

n = int(input("Digite o número de valores aleatórios (n): "))

valores_aleatorios = [random.randint(0, 100) for _ in range(n)]

soma_valores = sum(valores_aleatorios)

raiz_quadrada = math.sqrt(soma_valores)

print(f"A raiz quadrada da soma dos valores é: {raiz_quadrada}")
