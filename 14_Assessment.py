# Assessment
import random
import string

# Aufgabe 1
# Funktion schreiben "vol()" die das volumen einer Kugel ausgibt
import math
def vol(radius):
    volumen = (4/3)*math.pi*radius**3
    print(volumen)
    return volumen
vol(10)



# Funktion zum Prüfen ob Zahl in Bereich von bis?
def bereich_check (zahl, ug, og):
    #if zahl >= ug and zahl <= og:
    #besser:
    if zahl in range(ug, og+1):
        print("pass")
        return True
    else:
        print("Nicht in Bereich.")
print("bereich_check (10,5,20),", bereich_check(20,5,20))
# nur boolean wert:
def bereich_boolean(zahl, unten, oben):
    return zahl in range(unten, oben+1)
print(bereich_boolean(3,0,10))




# Funktion schreiben, die in einem String die kleine und großen Buchstaben zählt
def gross_klein(s):
    capital = 0
    lowercase = 0
    letters = list(s)
    print(letters)
    for buchstabe in letters:
        #print(buchstabe)
        if buchstabe.isupper():
            capital += 1
        elif buchstabe.islower():
            lowercase += 1
        else:
            print("Da war wohl ein Satz- /Leerzeichen")
    print("Ausgabe:")
    print("Anzahl Großbuchstaben: %r" %(capital))
    print("Anzahl Kleinbuchstaben: %r" %(lowercase))

beispielstring = "Hallo Herr Schmidt, wie geht es Ihnen an diesem schönen Dienstag?"
gross_klein(beispielstring)

print("Beginn jeder Wert nur einmal")
# Aus liste mit zufälligen Werten jeden vorkommenden Wert nur einmal in eine Liste aufnehmen
bsp_liste = [random.randint(1,10) for i in range(20)]
print(bsp_liste)
def einzig_liste(l):
    liste_e = []
    for element in l:
        print(element)
        x = element in liste_e
        if x == False:
            liste_e.append(element)
        else:
            print("War schon")
        print(liste_e)
    return liste_e
momo = einzig_liste(bsp_liste)
print(momo)

print("MARKER")


# Funktion zum Multiplizieren aller Zahlen in einer Liste
def multi(zahlen):
    produkt = 1
    for mu in zahlen:
        print("Multiplikator ist: %r" %produkt)
        print("mu ist: %r" %(mu))
        produkt = produkt*mu
        print("Produkt ist: %r" %(produkt))
    return produkt
testmulti = [1,2,3,-4]
bubu = multi(testmulti)
print(bubu)


def palindrom(wort):
    wort = wort.lower()
    rueckwaerts = wort[::-1]
    if wort == rueckwaerts:
        pali = True
    else:
        pali = False
    return pali
print(palindrom("Non"))


# Funktion zum Prüfen ob ein String ein Pangram ist
print("Marker Pangram")
def pangram(input):
    import string
    input = input.lower()       # alles Kleinbuchstaben
    test = []
    for element in input:       # Sonder und Leerzeichen löschen
        if element in string.ascii_lowercase:
            test.append(element)
    test = sorted(test)
    letters_set = set(test)
    letters = list(letters_set)
    letters = sorted(letters)
    kontrollstring = "".join(letters)
    print(kontrollstring)
    print(string.ascii_lowercase)
    if kontrollstring == string.ascii_lowercase:
        result = True
    else:
        result = False
    return result

print("SUPERMARKER")

def pangramm(s, alphabet = string.ascii_lowercase):
    print(alphabet)
    alphaset = set(alphabet)
    print(alphaset)
    print("hier")
    print(set(s.lower()))
    print(len(alphaset))
    print(len(set(s.lower())))
    return alphaset <= set(s.lower())

print(pangramm("Vogel Qua zwickt Johnys Pferd BimmJNLKN.!?"))
print("hallo??")
pangrammodotest = "bacöäöß?66test  Vogel Quax zwickt Johnys Pferd Bim."
print("Echtes Pangram mit Sonderzeichen etc: " + str(pangram(pangrammodotest)))

neuer_pg_test = "Typisch fiese Kater würden Vögel bloß zum Jux quälen.!1!!11!1?ä"
print("Echtes Pangram: " + str(pangram(neuer_pg_test)))

kein_pg = "bacöäöß?66test  Vo"
print("Kein PG sollte sein: " + str(pangram(kein_pg)))

















