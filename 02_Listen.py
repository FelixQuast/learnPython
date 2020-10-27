#
import random as ran

liste = [1, 2, 3]
print(liste)
a = len(liste)
print(a)

liste = liste + [4, 5]
print(liste)

liste.append(6)
liste.append(7)
print(liste)

liste.pop(6)

ran.shuffle(liste)
print(liste)

liste.sort()
print(liste)

neue_liste = ["a", "S", "d", "f"]
print(neue_liste)


#verschachtelte listen
v1 = [1,2,3]
v2 = [4,5,6]
v3 = [7,8,9]

matrix = [v1, v2, v3]

element = matrix[2][2]
print(element)