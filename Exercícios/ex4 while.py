#ingressos de cinema

# > perguntar idade
# > informar preço do ingresso (0 a 3 = de graça, 4 a 12 = 15R$, 12+ = 30R$)
# > digitar ''sair'' para encerrar o programa
# > depois de sair, mostrar quantas pessoas comparam ingressos, total de dinheiro e média de idade
from time import sleep

pessoas = int(0)
media_idades = int(0)
din_total = float(0)

print('O ingresso é gratuito para menos de 3 anos, custa R$15,00 para pessoas entre 4 a 12 anos e R$30,00 para maiores de 12 anos.')
while True:
    idade = input('Qual a idade: ')
    print('pessoa computada com sucesso...')
    if idade == 'sair':
        break
    idade = int(idade)
    sleep(1)
    if idade < 3:
        pessoas += 1
        media_idades += idade
    if idade in range(4, 12):
        pessoas += 1
        media_idades += idade
        din_total += 15
    if idade > 12:
        pessoas += 1
        media_idades += idade
        din_total += 30

print('Quantidade de pessoas: {} // Dinheiro arrecadado: {} // média de idades: {}'.format(pessoas, din_total, media_idades / pessoas))