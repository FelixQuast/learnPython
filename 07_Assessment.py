# Erstes Assessment

# Aufgabe 1:
# Beschreibungvon Zahlen, Strings, Listen, Tupel, Dictionaries
# Zahlen: Es gibt Integers und Floats

# Strings: Eingabe in Anführungszeichen oder zwischen Apostroph
#   Auswahl und änderung mäglich
a = "test"
b = 'test'
if a == b:
    print(True)
else:
    print(False)
print(a[2])
print("-------")
# Listen: sind stacks, also oben kommt was drauf/runter. Erstellung durch eckige Klammern
# Listen können alles mögliche enthalten und auch verschachtelt werden.
# Positionen können durch Anwahl der Position ihrer Elemente geändert werden

liste = [1, 3.14, "String", ["sub1", "sub2", "sub3"], True, 5, 5, 5]
print(liste)
liste.append("Anhang")      # hinten anhängen
print(liste)
liste.pop()                 # hinten löschen
print(liste)
liste.pop(2)                # Position 2 Löschen (also den dritten
print(liste)
c = liste.count(5)          # zählen wie oft 5 drin vorkommt
print(c)
neue_liste = [0,1,2,3,4,5,6,7,8,9]
d = neue_liste[5]
print("-------")

print(d)
neue_liste[5] = 6
print(neue_liste[5])
print("-------")

# tupel werden mit runden klammern erzeugt
# Ihre inhalte können gezielt über die Elementposition gelesen, nicht aber geändert werden
# für tupel gibt es nur wenige methoden -> count und index, also wie oft gibt es ein element und wo steht ein element erstmals
mein_tupel = ("test", 1, 2, 3.14, 2, 1, 3, 3, 4, 3, 5, 3)
print(type(mein_tupel))
print(mein_tupel[0])
e = mein_tupel.count(3)
f = mein_tupel.index(3)
print(e)
print(f)
print("-------")

