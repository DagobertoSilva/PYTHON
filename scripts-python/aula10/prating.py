note1 = float(input('What is your first note? '))
note2 = float(input('what is your second note? '))
media = (note1+note2)/2
print('Your media was: {:.1f}'.format(media))
#print('your media was goood, congratulations!!!!!!!'if media>= 6 else'your media was not good, to study more!!!!!') simplificade condicion
if media>=6:
    print('your media was goood, congratulations!!!!!!!')
else:
    print('your media was not good, to study more!!!!!')