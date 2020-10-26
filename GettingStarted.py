# Strings

str = "Das ist ein String!"
print(str)

a = str.upper()
print(a)

b = str.lower()
print(b)

c = str[0]
print(c)

d = str[4:7]
print(d)

e = str[4:]
print(e)

f = str.split()
print(f, type(f))

name = "hans"
alter = 34.123456789
print("%s ist %r Jahre alt" %(name, alter))

neuername = "Dieter"
flieskomma = 66.852
print("%s ist %40.10f Jahre alt" %(neuername, 66.852))

liste = ("hallo", 3.14, 35)
print("erstes: %s, zweites: %r, drittes: %r" %(liste))
print(type(liste))

g = "hallo"
h = "test"
i = 3.14
print('test 1: {}, test 2: {}, test 3: {}'.format(g, h, i))     #die klammern bleiben leer. Sollen an die stellen Platzhaler rein müssen diese im "format def werden

j = "Stuhl"
k = "1000000€"
print('Zu Verkaufen: {Ware}, Preis: {Preis}'.format(Ware = j, Preis = k))

