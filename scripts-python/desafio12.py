preco = float(input('Digite o preço do produto: '))
desconto = preco * (5/100)
novo_Preco= preco - desconto
print('o Novo preco do produto é {:.2f} R$'.format(novo_Preco))