# Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. 
# Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas

distancia = int(input("Digite a distância em KM: "))
peso = float(input("Digite o peso do pacote em KG: "))

if distancia <- 100:
    frete = 1
elif distancia >= 101 and distancia <= 300:
    frete = 1.5
else:
    frete = 2

if peso > 10:
    print(f"O valor do frete será {(peso * frete) + 10} reais")
else:
    print(f"O valor do frete será {peso * frete} reais")