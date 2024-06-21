# Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. 
# Cada personagem tem uma classe específica com requisitos de atributos. 
# Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), 
# os pontos de força e os pontos de magia atribuídos ao personagem. 
# O programa deve imprimir True se os pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras:
# Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
# Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
# Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.
# O programa deve imprimir False se os pontos de atributo não são consistentes com a classe escolhida.

classe = input("Escolha sua classe (guerreiro, mago ou arqueiro): ")
pontosForca = int(input("Digite seus pontos de força (1 a 20): "))
pontosMagia = int(input("Digite seus pontos de magia (1 a 20): "))

if classe == "guerreiro":
    if pontosForca >= 15 and pontosMagia <=10:
        print("True. Seus pontos de atributo são consistentes com a classe escolhida!")
    else:
        print("False. Seus pontos de atributo não são consistentes com a classe escolhida.")
elif classe == "mago":
    if pontosForca <= 10 and pontosMagia >= 15:
        print("True. Seus pontos de atributo são consistentes com a classe escolhida!")
    else:
        print("False. Seus pontos de atributo não são consistentes com a classe escolhida.")
else:
    if (pontosForca > 5 and pontosForca <= 15) and (pontosMagia > 5 and pontosMagia <= 15):
        print("True. Seus pontos de atributo são consistentes com a classe escolhida!")
    else:
        print("False. Seus pontos de atributo não são consistentes com a classe escolhida.")    