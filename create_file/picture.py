fa = open('a.png','r')

fb = open('b.png','w')
fb.write(fa.read())

fb.close()
fa.close()