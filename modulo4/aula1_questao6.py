experimentos = int(input("Digite a quantidade de experimentos: "))

contador,quantidade,c,r,s = 0,0,0,0,0

while experimentos != contador:
    tipo = input("Qual animal foi utilizado? (C) Coelho, (R) Rato ou (S) Sapo: ")
    quantidade = int(input("Digite a quantidade de cobaias utilizadas: "))

    contador +=1
    if tipo=="c" or tipo=="C":
        c += quantidade
    elif tipo=="r" or tipo=="R":
        r += quantidade
    elif tipo+"s" or tipo=="S":
        s += quantidade

total = c+r+s

print (f'O número total de cobaias utilizadas foi de {total}.')
print (f'Foram utilizados {c} Coelhos, {r} Ratos e {s} Sapos.')
print (f'Percentual de Coelhos: {c/total*100:2.2f}% / Percentual de Ratos: {r/total*100:2.2f}% / Percentual de Sapos: {s/total*100:2.2f}%')
