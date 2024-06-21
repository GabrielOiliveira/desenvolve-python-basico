def valida_cpf(cpf):

    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11

    if resto < 2:
        digito_verif1 = 0
    else:
        digito_verif1 = 11 - resto

    if digito_verif1 != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11

    if resto < 2:
        digito_verif2 = 0
    else:
        digito_verif2 = 11 - resto

    if digito_verif2 != int(cpf[10]):
        return False

    return True

cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
if valida_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")
