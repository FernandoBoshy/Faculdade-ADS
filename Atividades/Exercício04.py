def lerInt(mensagem):  # função para checar se o valor digitado é um numero INT ou não
    check = False
    while True:
        valor = str(input(mensagem))
        if valor.isnumeric():
            valor = int(valor)
            check = True
        else:
            print('Digite um valor numérico')
        if check:
            break
    return valor


def lerFloat(mensagem):  # função para checar se o valor digitado é um numero FLOAT ou não
    check = False
    while True:
        valor = str(input(mensagem))
        valor_check = valor.replace('.', '')
        try:
            if valor_check.isnumeric():
                valor = float(valor)
                check = True
            else:
                print('Digite um valor numérico')
            if check:
                break
        except:
            print('ocorreu algum erro inesperado...')
        else:
            pass
    return valor


def menu():  # função para gerar um menu
    print('''Escolha uma opção
1 - Cadastrar produto
2 - Consultar produto
3 - Remover produto
4 - Sair''')


def cadastrarProdutos(contador):  # função para cadastrar o produto e joga-lo em um dicionário
    codigo = ''
    produto = str(input('Digite o nome do produto: '))
    fabricante = str(input('Digite o fabricante do produto: ').lower())
    valor = lerFloat('Digite o valor do produto: ')
    codigo = contador

    produtos.update({'nome': produto, 'fabricante': fabricante, 'valor': valor, 'codigo': codigo})  # cria um dicionário com os 4 itens acima e os copia para a lista de produtos
    lista_produtos.append(produtos.copy())
    produtos.clear()


def consultarProdutos():  # função para consultar os produtos
    while True:
        print('1 - Consultar todos os produtos')
        print('2 - Consultar por código')
        print('3 - Consultar por fabricante')
        print('4 - voltar')
        consulta = lerInt('')  # opção a ser escolhida
        if consulta == 1:
            for x in lista_produtos:
                print('Nome: {:<12s} | Fabricante: {:<12s} | Valor: {:<7.2f} | Codigo: {:<5}'.format(x['nome'], x['fabricante'], x['valor'], x['codigo']))
        elif consulta == 2:
            while True:
                cod = lerInt('Digite o código do produto ou digite 0 para voltar: ')
                if cod == 0:
                    break
                for x in lista_produtos:
                    if cod == x['codigo']:
                        print('Nome: {:<12s} | Fabricante: {:<12s} | Valor: {:<7.2f} | Codigo: {:<5}'.format(x['nome'], x['fabricante'], x['valor'], x['codigo']))
                        break
        elif consulta == 3:
            while True:
                fab = str(input('Digite o fabricante ou digite 0 para voltar: ').lower())
                if fab == '0':
                    break
                for x in lista_produtos:
                    if fab == x['fabricante']:
                        print('Nome: {:<12s} | Fabricante: {:<12s} | Valor: {:<7.2f} | Codigo: {:<5}'.format(x['nome'], x['fabricante'], x['valor'], x['codigo']))
                break

        elif consulta == 4:
            break


def removerProduto():  # função para remover os produtos pelo código
    while True:
        cod = lerInt('Digite o código do produto para remove-lo: ')
        if cod == 0:
            break
        for x, y in enumerate(lista_produtos):
            if cod == y['codigo']:
                lista_produtos.pop(x)
        break


# Programa principal

print('Iniciando controle de estoque da mercearia Fernando Augusto de Oliveira - RU.3301034')

produtos = {'nome': '', 'fabricante': '', 'valor': 0, 'codigo': ''}  # variáveis iniciais
lista_produtos = []
contador = 0

while True:
    menu()
    op = lerInt('Digite: ')
    if op == 1:
        contador += 1
        cadastrarProdutos(contador)
    elif op == 2:
        consultarProdutos()
    elif op == 3:
        removerProduto()
    elif op == 4:
        break
    else:
        print('Opção inválida...')
print('Finalizando programa')