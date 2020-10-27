# Strings
import math
pi = math.pi
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

tupel = ("hallo", 3.14, 35)
print("erstes: %s, zweites: %r, drittes: %r" % (tupel))
print(type(tupel))

g = "hallo"
h = "test"
i = 3.14
print('test 1: {}, test 2: {}, test 3: {}'.format(g, h, i))     #die klammern bleiben leer. Sollen an die stellen Platzhaler rein müssen diese im "format def werden

j = "Stuhl"
k = "1000000€"
print('Zu Verkaufen: {Ware}, Preis: {Preis}'.format(Ware = j, Preis = k))
#oder oder oder oder oder oder
print('Zu Verkaufen: {Ware}, Preis: {Preis}'.format(Ware = "Tisch", Preis = "50"))

liste = ["String", pi, pi**2]
print(liste)
liste = liste + [666]
print(liste)
liste.append("test")
print(liste)
geklaut = liste.pop(1)
print(liste)
print(geklaut)

neue_liste = ["a", "d", "c", "b"]
print(neue_liste)
neue_liste.sort()
print(neue_liste)

vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
vector3 = [7, 8, 9]

matrix = [vector1, vector2, vector3]
print(vector1)
print(vector2)
print(vector3)
print(matrix)

test = matrix[1]
print(test)
print(type(test))
test2  = repr(test)
print(test2)
print(type(test2))

#test_string = "".join([str(_) for _ in a])


#print("probieren" + test_string)



