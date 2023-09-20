import math #importando todas as funções da biblioteca math
from math import sqrt #importando apenas a função de raiz quadrada da biblioteca math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
#raiz = sqrt(num) #apenas chamando sqrt da math
#print('a raiz quadrada de {} é {}'.format(num,math.ceil(raiz))) arredondando a raiz quadrada
print('a raiz quadrada de {} é {}'.format(num,raiz))
#print('a raiz quadrada de {} é {}'.format(num,sqrt(raiz)))  #apenas chamando sqrt da math
