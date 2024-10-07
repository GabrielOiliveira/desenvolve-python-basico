respondentes = int(input('Digite a quantidade de respondentes:'))
soma = 0
quantidade = respondentes

while quantidade > 0:
    soma += int(input('Digite a idade do respondente:'))
    quantidade -= 1

print (f'A média das idades dos respondentes é de {(soma/respondentes):.0f} anos.')
