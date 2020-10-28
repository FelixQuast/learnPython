# Schleifen
# Insbesondere for-loops sollenbesser verstanden werden



# 1. Beispiel:
liste = [2,3,4,5,6,7,8]
for zahl in liste:
    if zahl%2==0:
        print(zahl)



print("----------")
liste_tupel = [(11,12,13),(21,22,23),(31,32,33)]
for derganzekack in liste_tupel:
    print(derganzekack)
for (el1,dengel,spacko) in liste_tupel:
    print(dengel)



dictionary = {"Äpfel":4, "Bananen":30, "Mangos":3}
for item in dictionary:
    print(item)

for key,value in dictionary.items():
    print(key)
    print(value)


print("--------------------")
print("Hier gehts um range etc")

abc = list(range(0,10,1))
print(abc)

summe = 0
for number in range(1,10000000,1):
    summe = summe + 1/(number*number)

print(summe)
