print('Bem vindo a loja do Fernando Augusto de Oliveira - RU 3301034')
nome = str(input('Nome do produto: '))
preco = float(input('Preço do produto: ')) # variáveis
quant = int(input('Quantidade do produto: '))

if quant < 5: # até 4 unidades do produto
   print('Preço por un. do produto {}: R${:.2f}'.format(nome, preco))
   print('Desconto: 0%')
   print('Total a pagar: R${:.2f}'.format(preco * quant))
elif quant in range(5, 20): # entre 5 a 19 unidades do produto
   print('Preço por un. do produto {}: R${:.2f}'.format(nome, preco))
   print('Desconto: 3%')
   print('Total sem desconto: {:.2f}'.format(preco * quant))
   print('Total a pagar com desconto: R${:.2f}'.format(preco * 0.97 * quant))
elif quant in range(20, 100): # entre 20 a 99 unidades do produto
   print('Preço por un. do produto {}: R${:.2f}'.format(nome, preco))
   print('Desconto: 6%')
   print('Total sem desconto: {:.2f}'.format(preco * quant))
   print('Total a pagar com desconto: R${:.2f}'.format(preco * 0.94 * quant))
else: # 100 ou mais unidades do produto
   print('Preço por un. do produto {}: R${:.2f}'.format(nome, preco))
   print('Desconto: 10%')
   print('Total sem desconto: {:.2f}'.format(preco * quant))
   print('Total a pagar com desconto: R${:.2f}'.format(preco * 0.90 * quant))