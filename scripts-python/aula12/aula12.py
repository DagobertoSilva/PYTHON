name  = str(input('input your name: '))
if name == 'Dagoberto':
    print('Your name is beautiful!!')
elif name == 'joão' or name == 'Julia' or name == 'Maria':
    print('your name is very famous in Brasil')
elif name in 'Ana cláudia Jéssica Julieta':
    print('beuatiful name feminine')
else:
    print('your name is so normal!!')
print('have a good day {}'.format(name))