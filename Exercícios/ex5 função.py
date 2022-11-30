def borda(x=''):
    x = str(x)
    print('+', '-' * len(x), '+')
    print('|', x, '|')
    print('+', '-' * len(x), '+')

palavra = input('digita ae: ')
borda(palavra)