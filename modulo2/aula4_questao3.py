# Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. 
# O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. 
# Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados 
# e imprima ao final o preço total da compra.

nome_produto1 = input("\033[3mDigite o nome do produto 1: \033[0m")
preco_produto1 = float(input("\033[3mDigite o preço da unidade do produto 1: \033[0m"))
quantidade_produto1 = int(input("\033[3mDigite a quantidade do produto 1: \033[0m"))

nome_produto2 = input("\033[3mDigite o nome do produto 2: \033[0m")
preco_produto2 = float(input("\033[3mDigite o preço da unidade do produto 2: \033[0m"))
quantidade_produto2 = int(input("\033[3mDigite a quantidade do produto 2: \033[0m"))

nome_produto3 = input("\033[3mDigite o nome do produto 3: \033[0m")
preco_produto3 = float(input("\033[3mDigite o preço da unidade do produto 3: \033[0m"))
quantidade_produto3 = int(input("\033[3mDigite a quantidade do produto 3: \033[0m"))

print (f"Total R$:{(preco_produto1*quantidade_produto1) + (preco_produto2*quantidade_produto2) + (preco_produto3*quantidade_produto3):,.2f}")