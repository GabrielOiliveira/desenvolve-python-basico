# Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) 
# e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, 
# de acordo com as seguintes regras:
# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos
# C: Ou ter 60 anos  e trabalhado pelo menos 25.

sexo = input("Digite o seu gênero (M ou F): ")
idade = int(input("Digite sua idade: "))
tempoServico = int(input("Digite seu tempo de serviço (em anos): "))

if (sexo == "M" and idade > 65) or (sexo == "F" and idade > 60) or tempoServico >= 30 or (idade >= 60 and tempoServico >= 25):
    print("True. Você já pode se aposentar!")
else:
    print ("False. Você ainda não pode se aposentar.")