#nome = input('qual é o seu nome')
#print('prazer em te conhecer {:^^20}!'.format(nome))

n1 = int(input('digite um numero'))
n2 = int(input('Digite outro número'))
s = n1 + n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1 **n2

print(' a soma é {}, \no produto é {} \ne a divisão é {:.3f}'.format(s,m,d), end=' ')
print('\nDivisao inteira {} \ne potência {}'.format(di, e))