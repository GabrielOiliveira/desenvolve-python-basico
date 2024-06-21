# Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. 
# Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. 
# Lembre-se do operador do python % que retorna o resto de uma divisão.

valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))

if (valor1 + valor2) % 2 == 0:
    print("A soma dos dois valores é par!")
else:
    print("A soma dos dois valores é ímpar!")    