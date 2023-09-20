from math import pow,sqrt
cateto_oposto = int(input('Qual o valor do cateto oposto? '))
cateto_adjascente = int(input('Qual o valor do cateto adjascente? '))
hipotenusa = sqrt(pow(cateto_oposto,2)+pow(cateto_adjascente,2))
print('A hipotenusa é: {}'.format(hipotenusa))