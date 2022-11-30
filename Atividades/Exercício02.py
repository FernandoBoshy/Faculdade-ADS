print('Bem vindo a pizzaria do Fernando Augusto de Oliveira - RU 3301034')

pedido = float(0)
print('_' * 10, 'Cardápio', '_' * 10)
print('| Código | Sabores    | Média    | Grande   |')  # print do cardápio
print('|   21   | Napolitana | R$ 20,00 | R$ 26,00 |')
print('|   22   | Margherita | R$ 20,00 | R$ 26,00 |')
print('|   23   | Calabresa  | R$ 25,00 | R$ 32,50 |')
print('|   24   | Toscana    | R$ 30,00 | R$ 39,00 |')
print('|   25   | Portuguesa | R$ 30,00 | R$ 39,00 |')

while True:
    cod = 0
    tamanho = str(input('Tamanho M ou G: ').upper())  # digitar o tamanho em maiusculo ou minusculo não faz diferença
    if tamanho == 'M':  # tamanho médio escolhido
        try:
            cod = int(input('Código da pizza: '))
        except:
            print('\33[0;31mCódigo inválido\033[m')  # caso o código das pizzas seja inválido
            continue
        else:
            pass

        if cod == 21:
            print('Sabor Napolitana(média) adicionado ao pedido')  # elif's dos códigos das pizzas médias
            pedido += 20
        elif cod == 22:
            print('Sabor Margherita(média) adicionado ao pedido')
            pedido += 20
        elif cod == 23:
            print('Sabor Calabresa(média) adicionado ao pedido')
            pedido += 25
        elif cod == 24:
            print('Sabor Toscana(média) adicionado ao pedido')
            pedido += 30
        elif cod == 25:
            print('Sabor Portuguesa(média) adicionado ao pedido')
            pedido += 30
        else:
            print('\033[33mCódigo da pizza não encontrado...\033[m')
            continue
    elif tamanho == 'G':  # tamanho grande escolhido
        try:
            cod = int(input('Código da pizza: '))
        except:
            print('\33[0;31mCódigo inválido\033[m')  # caso o código das pizzas seja inválido
            continue
        else:
            pass

        if cod == 21:
            print('Sabor Napolitana(Grande) adicionado ao pedido')  # elif's dos códigos das pizzas grandes
            pedido += 26
        elif cod == 22:
            print('Sabor Margherita(Grande) adicionado ao pedido')
            pedido += 26
        elif cod == 23:
            print('Sabor Calabresa(Grande) adicionado ao pedido')
            pedido += 32.5
        elif cod == 24:
            print('Sabor Toscana(Grande) adicionado ao pedido')
            pedido += 39
        elif cod == 25:
            print('Sabor Portuguesa(Grande) adicionado ao pedido')
            pedido += 39
        else:
            print('\033[33mCódigo da pizza não encontrado...\033[m')
            continue
    else:
        print('\033[31mTamanho inválido\033[m')  # caso o código do tamanho seja inválido
        continue

    print('valor atual do pedido: R${:.2f}'.format(pedido))  # print da soma dos valores
    print('Deseja mais pizzas? (Aperte Enter para continuar, ou digite 0 para sair)')  # confirmação para adicionar mais pizzas
    x = input()
    if x == '0':  # digitar qualquer coisa além de 0 resulta em continuar
        break

print('O valor do seu pedido é de R${:.2f}'.format(pedido))  # valor final do pedido
