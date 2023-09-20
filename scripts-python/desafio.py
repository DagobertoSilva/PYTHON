nomeCompleto =str(input('Digite seu nome completo: ')).strip()
maiscula = nomeCompleto.upper()
minuscula = nomeCompleto.lower()
Quantidaletras = len(nomeCompleto) - nomeCompleto.count(' ')
Quantidaletrasfirstname = nomeCompleto.split


print('Nome completo: {}'.format(nomeCompleto))
print('Nome em Maiúsculo: {}'.format(maiscula))
print('Nome em minúsculo: {}'.format(minuscula))
print('Qauntidade de letras do nome: {}'.format(Quantidaletras))
print('Quantidade de letras do primeiro nome: {}'.format(nomeCompleto.find(' ')))
