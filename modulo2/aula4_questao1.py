# Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), 
# bem como o preço do metro quadrado da região em ponto flutuante. 
# Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.

# O terreno possui 250m2 e custa R$512,490.50

# Comente na linha acima de cada instrução uma breve descrição da instrução.

# Fórmulas:
# area_m2 = comprimento * largura
# preco_total = preco_m2 * area_m2

comprimento  = int(input("Digite o comprimento do terreno: "))
largura = int(input("Digite a largura do terreno: "))
preco_metro = float(input("Digite o preço do m2: "))

area_m2 = comprimento * largura
preco_total = preco_metro * area_m2

print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")