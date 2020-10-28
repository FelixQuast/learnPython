# Listen Abstraktion, auch List Comprehension

liste = []
for buchstabe in "wort":
    liste.append(buchstabe)

print(liste)


liste2 = [buchstabe for buchstabe in "Neues_Wort"]
print(liste2)

liste3 = [x**2 for x in range (1,11)]
print(liste3)

liste4 = [x for x in range(0,11) if x % 2 == 0]
print(liste4)

# umrechnen von celsius in fahrenheit:
celsius = [0,10,21.2,36.7]
fahrenheit = [ ((9/5*temp+32)) for temp in celsius]
print(fahrenheit)

liste5 = [x**2 for x in [x**2 for x in range(11)]]

print(liste5)