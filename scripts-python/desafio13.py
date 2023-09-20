salario_funcionario = float(input('Digite o valor do salário do funcionário: '))
aumento = (15/100) * salario_funcionario
novo_salario_funcionario = salario_funcionario + aumento

print('o nono salário do funcionário é {:.2f} R$'.format(novo_salario_funcionario))