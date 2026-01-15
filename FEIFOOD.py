# ------------------------------------
# FEIFOOD - Sistema de pedidos em Python
# ------------------------------------

#MODULOS------------------------------------
import os
from random import randint
from time import sleep
import json
import customkinter

#DICIONÁRIOS ------------------------------------
bd_alimentos = []

with open("bd_alimentos.json", "r", encoding="utf-8") as arquivo:
    bd_alimentos = json.load(arquivo)

bd_usuario = []

# carrega o banco de usuários existente
with open("bd_usuario.json", "r", encoding="utf-8") as arquivo:
    bd_usuario = json.load(arquivo) #armazena na lista bd_usuario

pedido = []

with open("pedido.json", "r", encoding="utf-8") as arquivo:
    pedido = json.load(arquivo) 


# MENU INICIAL
def menu_principal():
    print('------------------- BEM-VINDO AO FEIFOOD! -------------------')
    print('1 - Login')
    print('2 - Cadastro')
    print('3 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        sleep(1)
        limpar_tela()
        print('------ LOGIN ------')
        while True:
            email = input('Digite seu email: ')
            input_valido(email, menu_principal)
            senha = input('Digite sua senha 4 dígitos: ')
            input_valido(senha, menu_principal)
            if validar_usuario(email, senha) == True:
                limpar_tela()
                input('Login realizado com sucesso! \nAperte enter para continuar...')
                limpar_tela()
                menu_usuario()
                break
            else: 
                limpar_tela()
                print('--------------------------')
                print('Email ou senha incorretos!')
                sleep(2)
                print('1 - Tentar novamente')
                print('2 - Menu inicial')
                opcao_nova_tentativa = input('Escolha uma opção: ')
                if opcao_nova_tentativa != '1':
                    limpar_tela()
                    break
                else:
                    limpar_tela()
            
    elif opcao == '2':
        sleep(1)
        limpar_tela()
        print('------ CADASTRO ------')
        nome = input('Digite seu nome completo: ')
        input_valido(nome, menu_principal)
        cpf =  input('Digite seu CPF: ')
        input_valido(cpf, menu_principal)
        endereco = input('Digite seu endereço: ')
        input_valido(endereco, menu_principal)
        email = input('Digite seu email: ')
        input_valido(email, menu_principal)
        
        while True:
            senha = input('Digite sua senha 4 dígitos: ')
            if len(senha) == 4 and senha.isdigit(): #.isdigit() garante q são apenas números
                break
            else:
                print('A senha deve conter exatamente 4 números!')

        input_valido(senha, menu_principal)
        cadastro(nome, cpf, endereco, email, senha)
        sleep(4)
        limpar_tela()
        return menu_usuario()

    elif opcao == '3':
        sleep(1)
        limpar_tela()
        sair()
    else:
        sleep(1)
        limpar_tela()
        input('Opção inválida!\n Aperte enter para voltar ao menu inicial...')
        limpar_tela()
        menu_principal()  # volta ao menu inicial

# ------------------------------------ FUNÇÕES USUARIO
#VALIDAR USUÁRIO
def validar_usuario(email, senha):
    for usuario in bd_usuario:
        if usuario['email'] == email and usuario['senha'] == senha:
            return True
    return False


# CADASTRO
def cadastro(nome_completo, cpf, endereco, email, senha):
    dados_cadastro = {
        'nome': nome_completo,
        'cpf': cpf,
        'endereco': endereco,
        'email': email,
        'senha': senha
    }
    for usuario in bd_usuario:
        if usuario['email'] == email:
            sleep(2)
            limpar_tela()
            input("Esse usuário já foi cadastrado! \nAperte enter para voltar ao menu inicial...")
            limpar_tela()
            return menu_principal()

    bd_usuario.append(dados_cadastro)  
    print('Usuário cadastrado com sucesso!')

    # regrava o arquivo com a lista atualizada
    with open("bd_usuario.json", "w", encoding="utf-8") as arquivo:
        json.dump(bd_usuario, arquivo, ensure_ascii=False, indent=4)
    

# ------------------------------------ MENU DO USUÁRIO
def menu_usuario():
    print('--------- MENU DO USUÁRIO ---------')
    print('1 - Menu Pedido')
    print('2 - Buscar Alimento')
    print('3 - Avaliar Pedido')
    print('4 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        sleep(2)
        limpar_tela()
        return menu_pedido()

    elif opcao == '2':
        limpar_tela()
        print('------ BUSCAR ALIMENTO ------')
        sleep(2)
        nome = input('Digite o nome do alimento: ')
        input_valido(nome, menu_usuario)
        buscar_alimento(nome)
        sleep(2)
        print('1- para voltar ao menu anterior \n2 - Para sair')
        opcao_alimentos = input('Digite uma opção: ')
        if opcao_alimentos == '1':
            limpar_tela()
            sleep(2)
            menu_usuario()
        if opcao_alimentos == '2':
            limpar_tela()
            sleep(2)
            sair()
        else: 
            limpar_tela()
            input('Opção inválida!\n Aperte enter para voltar ao menu usuário...')
            limpar_tela()
            return menu_usuario()

    elif opcao == '3':
        limpar_tela()
        print('------ AVALIAR PEDIDO ------')
        sleep(2)
        protocolo = int(input('Digite o protocolo do pedido que quer avaliar: '))
        input_valido(protocolo, menu_usuario)
        limpar_tela()
        print('------ AVALIAR PEDIDO ------')
        print('Digite a avaliação do seu pedido: ')
        print('1 - Muito ruim \n2 - Ruim \n3 - Regular \n4 - Bom \n5 - Muito bom ')
        avaliacao = input('Digite uma opção: ')
        input_valido(avaliacao, menu_usuario)
        avaliar_pedido(protocolo, avaliacao)
        sleep(2)
        limpar_tela()
        print('Pedido avaliado com sucesso!')
        sleep(2)
        limpar_tela()
        print('------ AVALIAR PEDIDO ------')
        for p in pedido: #para cada pedido dentro da lista pedidos
            if p['protocolo'] == protocolo:
                print(f'Nome: {p["nome_usuario"]}')
                for i in p['itens']: #para cada item dentro da lista de itens do criar_pedido
                    print(f"Item: {i['nome_item']} | Quantidade: {i['qtd']} | Preço: R$ {i['preco']:.2f}")
                print(f"Total: {p['total']:.2f}")
                print(f"Protocolo: {p['protocolo']}")
                print(f"Avaliação: {p['avaliacao']}")
                input('\nAperte enter para continuar...')
                limpar_tela()
                return menu_usuario()

    elif opcao == '4':
        limpar_tela()
        sleep(2)
        return sair()
    else:
        limpar_tela()
        sleep(2)
        print('Opção inválida!\n')
        sleep(2)
        limpar_tela()
        return menu_usuario()


# ------------------------------------ MENU DO PEDIDO
def menu_pedido():
    print('--------- MENU DO PEDIDO ---------')
    print('1 - Criar Pedido')
    print('2 - Editar Pedido')
    print('3 - Excluir Pedido')
    print('4 - Adicionar ou Remover Item do Pedido')
    print('5 - Voltar ao Menu do Usuário')
    print('6 - Sair')

    opcao = input('Escolha uma opção: ')

    #CRIAR PEDIDO
    if opcao == '1':
        sleep(2)
        limpar_tela()
        print('------ CRIAR PEDIDO ------')
        protocolo = randint(1000, 9999)
        preco_total = 0
        sleep(2)
        nome = input('Digite seu nome: ')
        input_valido(nome, menu_pedido)
        item = input('Digite o nome do item: ')
        input_valido(item, menu_pedido)
        qtd = input('Digite a quantidade: ')
        input_valido(qtd, menu_pedido)

        for alimento in bd_alimentos:
            if alimento['nome'].strip().lower() == item.strip().lower():
                preco_total = float(alimento['preco']) * int(qtd)
                break
        else:
            sleep(1)
            limpar_tela()
            input('Item não encontrado! \nAperte enter para voltar ao menu pedido...')
            limpar_tela()
            return menu_pedido()

        novo_pedido = {
            'nome_usuario': nome,
            'itens': [{'nome_item': item, 'qtd': int(qtd), 'preco': float(preco_total)}],
            'protocolo': protocolo,
            'total': float(preco_total),
            'avaliacao': ""
            }
        pedido.append(novo_pedido)
        with open("pedido.json", "w", encoding="utf-8") as arquivo:
            json.dump(pedido, arquivo, ensure_ascii=False, indent=4)

        while True:
            sleep(2)
            limpar_tela()
            print('------ CRIAR PEDIDO ------')
            print('Desejar adicionar um novo item ao seu pedido? ')
            print('1 - Sim \n2 - Não')
            opcao = input('Digite uma opção: ')
            if opcao == '1':
                limpar_tela()
                sleep(2)
                print('------ CRIAR PEDIDO ------')
                item = input('Digite o nome do item: ')
                input_valido(item, menu_pedido)
                qtd = input('Digite a quantidade: ') 
                input_valido(qtd, menu_pedido)
                criar_pedido(item, qtd, protocolo)
            else:
                break
        sleep(2)
        limpar_tela()
        print('Pedido criado com sucesso!')
        sleep(3)
        limpar_tela()
        print('---- Detalhes do Pedido ----')
        for p in pedido: #para cada pedido dentro da lista pedidos
            if p['protocolo'] == protocolo:
                for i in p['itens']: #para cada item dentro da lista de itens do criar_pedido
                    print(f"Item: {i['nome_item']} | Quantidade: {i['qtd']} | Preço: R$ {i['preco']:.2f}")
                print(f"Total: {p['total']:.2f}")
                print(f"Protocolo: {p['protocolo']}")
                
        print('---------')
        print('1 - Menu usuário \n2 - Sair')
        opcao = input('Digite uma opção: ')
        if opcao == '1':
            sleep(2)
            limpar_tela()
            print('Entrando no menu usuário...')
            sleep(3)
            limpar_tela()
            menu_usuario()
        else:
            sleep(2)
            limpar_tela()
            sair()

    #EDITAR PEDIDO
    elif opcao == '2':
        sleep(2)
        limpar_tela()
        print('------ EDITAR PEDIDO ------')
        #edição do nome
        protocolo = int(input('Digite o protocolo do pedido que deseja editar: '))
        input_valido(protocolo, menu_pedido)
        sleep(2)
        print('---- Detalhes do Pedido ----')
        for p in pedido: #para cada pedido dentro da lista pedidos
            if p['protocolo'] == protocolo:
                print(f'Nome: {p["nome_usuario"]}')
                for i in p['itens']: #para cada item dentro da lista de itens do criar_pedido
                    print(f"Item: {i['nome_item']} | Quantidade: {i['qtd']} | Preço: R$ {i['preco']:.2f}")
                print(f"Total: {p['total']:.2f}")
                print(f"Protocolo: {p['protocolo']}")
        print('---------------------')
        print('1 - Editar o seu nome; \n2 - Editar os itens.')
        opcao_editar = input('Digite uma opção: ')
        input_valido(opcao_editar, menu_pedido)
        
        #editar nome
        if opcao_editar == '1':
            sleep(2)
            limpar_tela()
            print('------ EDITAR NOME ------')
            nome_novo = input('Digite o novo nome: ')
            editar_pedido(protocolo, nome=nome_novo)
            sleep(2)
            print('---- Detalhes do Pedido Editado ----')
            for p in pedido: #para cada pedido dentro da lista pedidos
                if p['protocolo'] == protocolo:
                    print(f'Nome: {p["nome_usuario"]}')
                    for i in p['itens']: #para cada item dentro da lista de itens do criar_pedido
                        print(f"Item: {i['nome_item']} | Quantidade: {i['qtd']} | Preço: R$ {i['preco']:.2f}")
                    print(f"Total: {p['total']:.2f}")
                    print(f"Protocolo: {p['protocolo']}")
            print('1 - Menu usuário \n2 - Sair')
            opcao = input('Digite uma opção: ')
            if opcao == '1':
                sleep(2)
                limpar_tela()
                print('Entrando no menu usuário...')
                sleep(3)
                limpar_tela()
                menu_usuario()
            else:
                sleep(2)
                limpar_tela()
                sair()
                    
                
    #edicao dos itens
        elif opcao_editar == '2':
            sleep(2)
            limpar_tela()
            print('------ EDITAR ITEM ------')
            while True:
                item_antigo = input('Digite o item que deseja editar: ').lower()
                item_novo = input('Digite o novo item: ').lower()
                nova_qtd = input('Digite a nova quatidade: ')
                editar_pedido(protocolo, item_antigo=item_antigo, item_novo=item_novo, nova_qtd=int(nova_qtd))
                print('Deseja editar outro item do seu pedido? ')
                print('1 - Sim \n2 - Não')
                continuar = input('Digite uma opção: ')
                if continuar != '1':
                    sleep(2)
                    limpar_tela()
                    break
                else:
                    sleep(2)
                    limpar_tela()
        print('---- Detalhes do Pedido Editado ----')
        for p in pedido: #para cada pedido dentro da lista pedidos
            if p['protocolo'] == protocolo:
                print(f'Nome: {p["nome_usuario"]}')
                for i in p['itens']: #para cada item dentro da lista de itens do criar_pedido
                    print(f"Item: {i['nome_item']} | Quantidade: {i['qtd']} | Preço: R$ {i['preco']:.2f}")
                print(f"Total: {p['total']:.2f}")
                print(f"Protocolo: {p['protocolo']}")
        print()
        print('1 - Menu usuário \n2 - Sair')
        opcao = input('Digite uma opção: ')
        if opcao == '1':
            sleep(2)
            limpar_tela()
            print('Entrando no menu usuário...')
            sleep(3)
            menu_usuario()
        else:
            sleep(2)
            limpar_tela()
            sair()
            
    elif opcao == '3':
        sleep(2)
        limpar_tela()
        print('------ EXCLUIR PEDIDO ------')
        protocolo = input('Digite o protocolo do pedido que deseja excluir: ')
        input_valido(protocolo, menu_pedido)
        protocolo = int(protocolo)
        excluir_pedido(protocolo)
        sleep(2)
        input('Pedido excluido com sucesso! \nAperte enter para voltar ao menu usuário... ')
        limpar_tela()
        return menu_usuario()

    elif opcao == '4':
        limpar_tela()
        sleep(1)
        print('1 - Adicionar Item \n2 - Remover Item ')
        opcao = input('Digite uma opção: ')
        if opcao == '1':

            #ADICIONAR ITEM
            sleep(2)
            limpar_tela()
            print('------ ADICIONAR ITEM AO PEDIDO ------')
            protocolo = int(input('Digite o protocolo do pedido: '))
            input_valido(protocolo, menu_pedido)
            item = input('Digite o nome do item que deseja adicionar: ')
            input_valido(item, menu_pedido)
            qtd = input('Digite a quantidade: ')
            input_valido(qtd, menu_pedido)
            adicionar_alimento(protocolo, item, qtd)
            sleep(2)
            limpar_tela()
            print('------ ADICIONAR ITEM AO PEDIDO ------')
            print('Item adicionado com sucesso!')
            print()
            print('---- Detalhes do Pedido ----')
            for p in pedido: 
                if p['protocolo'] == protocolo:
                    for i in p['itens']: 
                        print(f"Item: {i['nome_item']} | Quantidade: {i['qtd']} | Preço: R$ {float(i['preco']):.2f}")
                    print(f"Total: {p['total']:.2f}")
                    print(f"Protocolo: {p['protocolo']}")
                    input('\nAperte enter para voltar o menu pedido...')
                    limpar_tela()
                    return menu_pedido()
                
        elif opcao == '2':
            
            #REMOVER ITEM
            sleep(2)
            limpar_tela()
            print('------ REMOVER ITEM DO PEDIDO ------')
            protocolo = int(input('Digite o protocolo do pedido: '))
            item = input('Digite o item que deseja remover: ')
            remover_alimento(protocolo, item)
            limpar_tela()
            print('Item removido com sucesso!')
            sleep(2)
            print('---- Detalhes do Pedido ----')
            encontrado = False
            for p in pedido: 
                if p['protocolo'] == protocolo:
                    encontrado = True
                    if len(p['itens']) == 0:
                        print("Não há mais itens neste pedido.")
                    else:
                        for i in p['itens']: 
                            print(f"Item: {i['nome_item']} | Quantidade: {i['qtd']} | Preço: R$ {float(i['preco']):.2f}")
                        print(f"Total: {p['total']:.2f}")
                        print(f"Protocolo: {p['protocolo']}")
                        break
            if not encontrado:
                print('Pedido não econtrado!')

            input('\nAperte enter para voltar o menu pedido...')
            limpar_tela()
            return menu_pedido()
        else:
            sleep(2)
            limpar_tela()
            input('Opção inválida! Aperte enter para voltar ao menu pedido...')
            limpar_tela()
            return menu_pedido()


    elif opcao == '5':
        sleep(2)
        limpar_tela()
        return menu_usuario()
    
    elif opcao == '6':
        sleep(2)
        limpar_tela()
        return sair()
    
    else:
        sleep(2)
        limpar_tela()
        print('Opção inválida! \nAperte enter para voltar ao menu pedido... ')
        limpar_tela()
        menu_pedido()

# ------------------------------------ FUNÇÕES DO PEDIDO
#FUNÇÃO CRIAR PEDIDO
def criar_pedido(item, qtd, protocolo):
    preco_total = 0
    encontrado = False #se não mudar para True o alimento não foi encontrado

    for alimento in bd_alimentos:
        if alimento['nome'].strip().lower() == item.strip().lower():
            preco_total = float(alimento['preco']) * int(qtd)
            encontrado = True
            break
    if not encontrado: #se o alimento não foi encontrado
        input('Item não encontrado! \nAperte enter para voltar ao menu pedido... ')
        return menu_pedido()

    for p in pedido:
        if p['protocolo'] == protocolo:
            p['itens'].append({'nome_item': item, 'qtd': qtd, 'preco': preco_total})
            p['total'] += preco_total

            with open("pedido.json", "w", encoding="utf-8") as arquivo:
                json.dump(pedido, arquivo, ensure_ascii=False, indent=4)
            return

#FUNÇÃO EDITAR PEDIDO
def editar_pedido(protocolo, nome = None, item_antigo = None, item_novo = None, nova_qtd = None):
    pedido_encontrado = False

    for p in pedido:
        if p['protocolo'] == protocolo:
            pedido_encontrado = True
            if nome != None:
                p['nome_usuario'] = nome

            if item_antigo is not None:
                item_encontrado = False
                for i in p['itens']:
                    if i['nome_item'].strip().lower() == item_antigo.strip().lower():
                        i['nome_item'] = item_novo
                        i['qtd'] = int(nova_qtd)
                    

                        for alimento in bd_alimentos:
                            if alimento['nome'].strip().lower() == item_novo.strip().lower():
                                item_encontrado = True
                                preco_unitario = float(alimento['preco'])
                                i['preco'] = preco_unitario * i['qtd']
                                break
                        break
                if not item_encontrado:
                    input('Nome do Item inválido! \nAperte enter para voltar ao menu pedido... ')
                    return  menu_pedido()
                
            p['total'] = sum(item['preco'] for item in p['itens']) #pega cada item do dicionario de itens, seleciona o preco e soma armazenado no campo total
            break
    if not pedido_encontrado:
        input('Protocolo inválido! \nAperte enter para voltar ao menu pedido... ')
        return menu_pedido()
    
    with open("pedido.json", "w", encoding="utf-8") as arquivo:
        json.dump(pedido, arquivo, ensure_ascii=False, indent=4)
                

#EXCLUIR PEDIDO
def excluir_pedido(protocolo):
    print('Excluindo pedido...')
    for p in pedido:
        if p['protocolo'] == protocolo:
            pedido.remove(p)
            with open("pedido.json", "w", encoding="utf-8") as arquivo:
                json.dump(pedido, arquivo, ensure_ascii=False, indent=4)
            break

#BUSCAR ALIMENTOS
def buscar_alimento(nome):
    for alimento in bd_alimentos:
        if alimento['nome'].strip().lower() == nome.strip().lower():
            sleep(1)
            limpar_tela()
            print('Alimento encontrado!')
            sleep(3)
            limpar_tela()
            print('---- Detalhes do Item ----')
            print(f"Nome: {alimento['nome']} | \nPreço: {alimento['preco']} | \nSabor: {alimento['sabor']} | \nValidade: {alimento['validade']} |")
            input('\nAperte enter para continuar...')
            limpar_tela()
            break
    else:
        sleep(1)
        limpar_tela()
        input('Alimento não encontrado! \nAperte enter para voltar ao menu usuário ...')
        limpar_tela()
        return menu_usuario()

#ADICIONAR ALIMENTO
def adicionar_alimento(protocolo, item, qtd):
    alimento_encontrado = False

    for alimento in bd_alimentos:
        if alimento['nome'].strip().lower() == item.strip().lower():
            alimento_encontrado = True
            preco_unitario = float(alimento['preco'])
            for i in pedido:
                if i['protocolo'] == protocolo:
                    i['itens'].append({
                        'nome_item': item,
                        'qtd': int(qtd),
                        'preco': preco_unitario * int(qtd)
                    })
                    preco_total = 0
                    for item_atual in i['itens']:
                        preco_total += float(item_atual['preco']) * int(item_atual['qtd'])
                    i['total'] = preco_total

                    with open("pedido.json", "w", encoding="utf-8") as arquivo:
                        json.dump(pedido, arquivo, ensure_ascii=False, indent=4)

    if not alimento_encontrado:
        limpar_tela()
        sleep(2)
        print('Item não encontrado!')
        input('Aperte enter para voltar ao menu pedido...')
        limpar_tela()
        return menu_pedido()

#REMOVER ALIMENTOS
def remover_alimento(protocolo, item):
    item_encontrado = False
    protocolo_encontrado = False
    item_encontrado_pedido = False
    alterou = False

    for alimento in bd_alimentos:
        if alimento['nome'].strip().lower() == item.strip().lower():
            item_encontrado = True
            break

    if not item_encontrado:
        input('Item inválido! \nAperte enter para voltar ao menu pedido ...')
        return menu_pedido()
    
    for p in pedido:
        if p['protocolo'] == protocolo:
            protocolo_encontrado = True
            for i in p['itens']:
                if i['nome_item'].strip().lower() == item.strip().lower():
                    item_encontrado_pedido = True
                    p['itens'].remove(i)
                    p['total'] -= float(i['preco'])
                    alterou = True
                    break
            break 

    if not item_encontrado_pedido:
        input('Item não está no pedido! \nAperte enter para voltar ao menu pedido... ')
        return menu_pedido()
    
    if not protocolo_encontrado:
        input('Protocolo inválido! \nAperte enter para voltar ao menu pedido... ')
        return menu_pedido()
    
    if alterou:
        with open("pedido.json", "w", encoding="utf-8") as arquivo:
            json.dump(pedido, arquivo, ensure_ascii=False, indent=4)

        return 



#------------------------------------ OUTRAS FUNÇÕES
def avaliar_pedido(protocolo, avaliacao):
    pedido_encontrado = False

    for p in pedido:
        if p['protocolo'] == protocolo:
            p['avaliacao'] = avaliacao
            pedido_encontrado = True
            break

    if not pedido_encontrado:
        print('Protocolo inválido!')
        return
    
    with open("pedido.json", "w", encoding="utf-8") as arquivo:
        json.dump(pedido, arquivo, ensure_ascii=False, indent=4)
            

def input_valido(valor, tela): 
    if not valor:  # se estiver vazio ou só espaços
        print("Entrada inválida! Tente novamente.")
        input('Aperte enter para continuar ...')
        limpar_tela()
        return tela()

def sair():
    print("Saindo do sistema... Até logo!")
    exit()

def limpar_tela():
    os.system('cls')
# ------------------------------------ EXECUÇÃO PRINCIPAL

while True:
    menu_principal()
