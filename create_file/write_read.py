f = open('12345.txt','w')
f.write('12345')
f.close()

f = open('12345.txt','r')
print f.read()
f.close()