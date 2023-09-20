largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area_parede = largura * altura
litro = area_parede/2

print('a largura da parede é {}\n a altura da parede é {}\n a área da parede é: {:.2f}M²\nsão necessários {} litros de tinta para pintar a parede'.format(largura,altura,area_parede,litro))