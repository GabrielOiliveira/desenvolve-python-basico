import csv

def ler_usuarios():
    usuarios = {}
    ultimo_id = 0
    try:
        with open('usuarios.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                id = int(row[0])
                usuarios[id] = {'nome': row[1], 'senha': row[2], 'tipo': row[3]}
                if id > ultimo_id:
                    ultimo_id = id
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
    return usuarios, ultimo_id

def criar_usuario(usuarios, nome, senha, tipo, ultimo_id):
    id = ultimo_id + 1
    usuarios[id] = {'nome': nome, 'senha': senha, 'tipo': tipo}
    
    with open('usuarios.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, nome, senha, tipo])
    
    print(f"Usuário {nome} criado com sucesso!")
    return id

def listar_usuarios(usuarios):
    print("Lista de Usuários:")
    for id, info in usuarios.items():
        print(f'ID: {id}, Nome: {info["nome"]}, Tipo: {info["tipo"]}')

def atualizar_usuario(usuarios, id, nome=None, senha=None, tipo=None):
    if id in usuarios:
        if nome:
            usuarios[id]['nome'] = nome
        if senha:
            usuarios[id]['senha'] = senha
        if tipo:
            usuarios[id]['tipo'] = tipo
        salvar_usuarios(usuarios)
        print(f"Usuário ID {id} atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")

def remover_usuario(usuarios, id):
    if id in usuarios:
        del usuarios[id]
        salvar_usuarios(usuarios)
        print(f"Usuário ID {id} removido com sucesso!")
    else:
        print("Usuário não encontrado.")

def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'NOME', 'SENHA', 'TIPO'])
        for id, info in usuarios.items():
            writer.writerow([id, info['nome'], info['senha'], info['tipo']])

def ler_produtos():
    produtos = {}
    try:
        with open('produtos.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                id = int(row[0])
                produtos[id] = {'nome': row[1], 'preco': float(row[2]), 'quantidade': int(row[3])}
    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
    return produtos

def criar_produto(produtos, nome, preco, quantidade):
    id = len(produtos) + 1
    produtos[id] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
    
    with open('produtos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, nome, preco, quantidade])
    
    print(f"Produto {nome} criado com sucesso!")

def listar_produtos(produtos):
    print("Lista de Produtos:")
    for id, info in produtos.items():
        print(f'ID: {id}, Nome: {info["nome"]}, Preço: R${info["preco"]:.2f}, Quantidade: {info["quantidade"]}')

def buscar_produto(produtos, nome):
    for id, info in produtos.items():
        if info['nome'].lower() == nome.lower():
            print(f'ID: {id}, Nome: {info["nome"]}, Preço: R${info["preco"]:.2f}, Quantidade: {info["quantidade"]}')
            return
    print("Produto não encontrado.")

def atualizar_produto(produtos, id, nome=None, preco=None, quantidade=None):
    if id in produtos:
        if nome:
            produtos[id]['nome'] = nome
        if preco is not None:
            produtos[id]['preco'] = preco
        if quantidade is not None:
            produtos[id]['quantidade'] = quantidade
        salvar_produtos(produtos)
        print(f"Produto ID {id} atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

def remover_produto(produtos, id):
    if id in produtos:
        del produtos[id]
        salvar_produtos(produtos)
        print(f"Produto ID {id} removido com sucesso!")
    else:
        print("Produto não encontrado.")

def salvar_produtos(produtos):
    with open('produtos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'NOME', 'PREÇO', 'QUANTIDADE'])
        for id, info in produtos.items():
            writer.writerow([id, info['nome'], info['preco'], info['quantidade']])

def listar_produtos_por_nome(produtos):
    produtos_ordenados = sorted(produtos.items(), key=lambda x: x[1]['nome'])
    print("Lista de Produtos Ordenados por Nome:")
    for id, info in produtos_ordenados:
        print(f'ID: {id}, Nome: {info["nome"]}, Preço: R${info["preco"]:.2f}, Quantidade: {info["quantidade"]}')

def listar_produtos_por_preco(produtos):
    produtos_ordenados = sorted(produtos.items(), key=lambda x: x[1]['preco'])
    print("Lista de Produtos Ordenados por Preço:")
    for id, info in produtos_ordenados:
        print(f'ID: {id}, Nome: {info["nome"]}, Preço: R${info["preco"]:.2f}, Quantidade: {info["quantidade"]}')

usuarios, ultimo_id = ler_usuarios()
produtos = ler_produtos()

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Menu de Usuários")
        print("2. Menu de Produtos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_usuarios()
        elif opcao == '2':
            menu_produtos()
        elif opcao == '3':
            break

def menu_usuarios():
    global ultimo_id
    while True:
        print("\n--- Menu Usuários ---")
        print("1. Criar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do usuário: ")
            senha = input("Digite a senha do usuário: ")
            tipo = input("Digite o tipo de usuário: ")
            ultimo_id = criar_usuario(usuarios, nome, senha, tipo, ultimo_id)
            listar_usuarios(usuarios)

        elif opcao == '2':
            listar_usuarios(usuarios)

        elif opcao == '3':
            id = int(input("Digite o ID do usuário a atualizar: "))
            nome = input("Digite o novo nome do usuário (pressione Enter para manter o atual): ")
            senha = input("Digite a nova senha do usuário (pressione Enter para manter a atual): ")
            tipo = input("Digite o novo tipo do usuário (pressione Enter para manter o atual): ")
            atualizar_usuario(usuarios, id, nome if nome else None, senha if senha else None, tipo if tipo else None)

        elif opcao == '4':
            id = int(input("Digite o ID do usuário a deletar: "))
            remover_usuario(usuarios, id)

        elif opcao == '5':
            break

def menu_produtos():
    while True:
        print("\n--- Menu Produtos ---")
        print("1. Criar Produto")
        print("2. Listar Produtos")
        print("3. Buscar Produto")
        print("4. Atualizar Produto")
        print("5. Deletar Produto")
        print("6. Listar Produtos Ordenados por Nome")
        print("7. Listar Produtos Ordenados por Preço")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            criar_produto(produtos, nome, preco, quantidade)

        elif opcao == '2':
            listar_produtos(produtos)

        elif opcao == '3':
            nome = input("Digite o nome do produto a buscar: ")
            buscar_produto(produtos, nome)

        elif opcao == '4':
            id = int(input("Digite o ID do produto a atualizar: "))
            nome = input("Digite o novo nome do produto (pressione Enter para manter o atual): ")
            preco = input("Digite o novo preço do produto (pressione Enter para manter o atual): ")
            quantidade = input("Digite a nova quantidade do produto (pressione Enter para manter a atual): ")
            atualizar_produto(produtos, id, nome if nome else None, float(preco) if preco else None, int(quantidade) if quantidade else None)

        elif opcao == '5':
            id = int(input("Digite o ID do produto a deletar: "))
            remover_produto(produtos, id)

        elif opcao == '6':
            listar_produtos_por_nome(produtos)

        elif opcao == '7':
            listar_produtos_por_preco(produtos)

        elif opcao == '8':
            break

menu_principal()

