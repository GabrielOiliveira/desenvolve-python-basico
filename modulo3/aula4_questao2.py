# Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. 
# Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5.

avaliacao = int(input("Digite a sua avaliação de um filme em uma escala de 1 a 5: "))

if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
else:
    print("Ruim.")