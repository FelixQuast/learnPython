# tupel


tupel = ("test", 1,2)
print(tupel)
print(type(tupel))
tupel2 = (3,True)
tupel = tupel + tupel2
print(tupel)

tup2 = (1, 3, 6, 2, False, 44.5, "test", True, 5,2,2,2,2,3)
l = len(tup2)
print(l)

value = tup2[1]
print(value)

print("------------------------------")

#position eines Elementes finden
a = tup2.index(5)
print(a)

# zählen wie oft etwas in einem Tupel steckt
b = tup2.count(2)
print(b)

