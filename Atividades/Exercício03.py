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


def volumeFeijoada(op):  # função da quantidade de feijoada
    while True:
        try:  # input da quantidade de feijoada
            quant = int(input('Quantidade de feijoada em ml: '))
        except:
            print('Digite um valor numérico')
        else:  # quantidade abaixo de 300 ou acima de 5000
            if quant < 300 or quant > 5000:
                print('Quantidade fora do escopo')
            else:
                break
    if op == 1:  # checagem da opção do tipo de feijoada
        return quant * 0.08
    if op == 2:
        return quant * 0.08 * 1.25
    if op == 3:
        return quant * 0.08 * 1.5
    else:
        print('opção inválida')


def opcaoFeijoada():  # função de qual opção de feijoada vai ser escolhida
    while True:
        opcao = lerInt('Qual opção de feijoada (1-básica 2-premium 3-suprema): ')
        if opcao > 3 or opcao < 1:
            print('Opção inválida')
            continue
        else:
            break

    return opcao


def acompFeijoada(mensagem):  # função para escolher os acompanhamentos
    valor = float(0)
    while True:
        try:  # try para a adição do acompanhamento
            op = int(input(mensagem))
        except:
            print('Digite um valor numérico')
        else:  # if's das opções de acompanhamento
            if op == 1:
                print('Opção - 200g de arroz')
                valor += 5
            elif op == 2:
                print('Opção - 150g farofa')
                valor += 6
            elif op == 3:
                print('Opção - 100g couve')
                valor += 7
            elif op == 4:
                print('Opção - laranja descascada')
                valor += 3
            else:
                print('Fechando pedido')
                break
    return valor


# início programa

valorfinal = 0

# print do menu
print('''
Bem vindo a feijoada do Fernando Augusto de Oliveira - RU 3301034
Iniciando menu de feijoada
\33[0;32mPrimeiro\33[m - Digite o tipo de feijoada desejada
1 -- Feijoada básica (Feijão + paiol + costelinha)
2 -- Feijoada Premium (Feijão + paiol + costelinha + partes de porco)
3 -- Feijoada Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)
\33[0;32mSegundo\33[m - Digite a quantidade de feijoada desejada (entre 300ml a 5000ml)
\33[0;32mTerceiro\33[m - Digite o código dos acompanhamentos
1 -- 200g de arroz
2 -- 150g de farofa
3 -- 100g de couve flor
4 -- 1un laranja descascada
outro valor -- Sair
''')

while True:  # programa principal
    valorfinal += volumeFeijoada(opcaoFeijoada()) + acompFeijoada('Acompanhamentos\n1-arroz\n2-farora\n3-couve-flor\n4-laranja\noutros valores = sair: ')
    break
print('Seu pedido vai custar R${:.2f}'.format(valorfinal))
