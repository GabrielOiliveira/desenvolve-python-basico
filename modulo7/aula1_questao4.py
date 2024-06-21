numero = input("Digite o número de celular: ")

numero = numero.replace(" ", "").replace("-", "")

if len(numero) == 8:
    numero_completo = f"9{numero[:4]}-{numero[4:]}"
elif len(numero) == 9 and numero.startswith("9"):
    numero_completo = f"{numero[:5]}-{numero[5:]}"
else:
    print("Número inválido.")
    exit()

print(f"Número completo: {numero_completo}")
