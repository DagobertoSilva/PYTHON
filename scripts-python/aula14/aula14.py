''' for c in range(0,number):
    print(c)
print('END') '''

# c = 1
# while c <10:
#     print(c)
#     c = c+1
# print('END')

N = 1 
par = impar = 0
while N != 0:
    N = int(input('Digite um número: '))
    if N != 0:
        if N % 2 == 0:
            par +=1
        else:
            impar +=1
print('you inputed {} par numbers\nyou inputed {}  impars numbers'.format(par, impar))    
print('END')