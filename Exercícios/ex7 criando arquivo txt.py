def leiaInt(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):
    try:
        ar = open(nomeArquivo, 'rt')
        ar.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criaArquivo(nomeArquivo):
    try:
        ar = open(nomeArquivo, 'wt+')
        ar.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} criado com sucesso\n'.format(nomeArquivo))

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        ar = open(nomeArquivo, 'at')
    except:
        print('Erro no cadastro do arquivo')
    else:
        ar.write('{}: {} \n'.format(nomeJogo, nomeVideogame))
    finally:
        ar.close()

def lerArquivo(nomeArquivo):
    try:
        ar = open(nomeArquivo, 'rt')
    except:
        print('Problema na leitura do arquivo')
    else:
        print(ar.read())
    finally:
        ar.close()

#Programa ################
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo encontrado')
else:
    print('Arquivo não encontrado')
    criaArquivo(arquivo)
while True:
    for menu in range(0, 4):
        if menu == 0:
            print('MENU')
        if menu == 1:
            print('1 - Cadastrar jogo')
        if menu == 2:
            print('2 - Ler lista de jogos')
        if menu == 3:
            print('3 - Sair')
    opcao = leiaInt('Escolher opção: ', 1, 3)
    if opcao == 1:
        print('Cadastrar jogo:')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif opcao == 2:
        print('Lista de jogos')
        lerArquivo(arquivo)
    elif opcao == 3:
        print('Saindo...')
        break