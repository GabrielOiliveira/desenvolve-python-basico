# Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. 
# Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de 
# tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. 
# O programa deve imprimir True, permitindo o ingresso do participante no clube, se:

# -tiver entre 16 e 18 anos
# -já tiver jogado pelo menos 3 jogos
# -já ter vencido pelo menos 1 jogo, 

# Sua expressão deve imprimir False caso contrário. 
# Aqui está um exemplo de interação com seu código no terminal, com entradas de dados destacadas em negrito e 
# as impressões de seu código em itálico (apenas para facilitar sua visualização).

# Digite sua idade: 17
# Já jogou pelo menos 3 jogos de tabuleiro? True
# Quantos jogos já venceu? 2
# Apto para ingressar no clube de jogos de tabuleiro: True

idade = int(input("Digite a sua idade: "))

if idade >= 16 and idade <= 18:
    jogos = int(input("Você já jogou pelo menos 3 jogos de tabuleiro? Responda 1 para SIM ou 0 para NÃO: "))
    if jogos:
        vitorias = int(input("Quantos jogos você já venceu? "))
        if vitorias >= 1:
            print ("True")
        else: 
            print ("False")        
    else: 
        print ("False")     
else:
    print ("False")