meses = {
    '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
    '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
    '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
}

data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

dia, mes, ano = data_nascimento.split('/')

mes_extenso = meses.get(mes)

print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
