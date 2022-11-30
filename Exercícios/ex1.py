produto = float(input('preço do produto: '))
desc = int(input('porcentagem de desconto: '))
p = desc / 100
prod_desc = produto - (produto * p)
print('o produto custa {:.2f} e com desconto de {}% custa {:.2f}.'.format(produto, desc, prod_desc))

