# Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. 
# Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:

# 86 graus Fahrenheit são 30 graus Celsius.

temperatura = int(input("Digite a temperatura em graus Fahrenheit: "))
valor_Celsius = int((temperatura - 32) * (5/9))

print (f"{temperatura} graus Fahrenheit são {valor_Celsius} graus Celsius.")