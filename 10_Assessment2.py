# Aufgabe 1
# Gib aus einem String alle Wörter aus, die mit "s" beginnen

string = "Gebe nur solche Wörter in diesem Satz aus, die mit einem s starten"

s = string.split()
print(s)
index = 0
liste = []
for wort in s:
    if wort[0] == "s" or wort[0] == "S":
        print(wort)
        liste.append(wort)
        print(liste)



#gerade_zahlen_bis_zehn = []
gerade_zahlen_bis_zehn = [x for x in range(0,11) if x%2 ==0]
print(gerade_zahlen_bis_zehn)
# bessere Lösung:
gerade_zahlen_bis_zehn_v2 = list(range(0,11,2))
print(gerade_zahlen_bis_zehn_v2)
print("marker")


#alle zahlen von 1 bis 50, die duch 3 teilbar sind
zahlen_teilbar_durch_drei = [x for x in range(1,51) if x%3 ==0]
print(zahlen_teilbar_durch_drei)


# wörter in string mit gerader Zeichenzahl finden, ausgebn mit dem Wort "gerade!
neuer_string = "Gebe alle Wörter dieses Satzes aus, die eine gerade Anzahl an Zeichen hat."
neuer_string = neuer_string.replace(",", "")
neuer_string = neuer_string.replace(".", "")
print(neuer_string)
neues_s = neuer_string.split()
print(neues_s)
worter_mit_gerader_zeichenzahl = [wortx for wortx in neues_s if len(wortx) % 2 == 0]
print(worter_mit_gerader_zeichenzahl)


# Ausgabe ganzer Zahlen von 1 bis 100, mit allem was durch 3 teilbar ist ersetzt durch "Buzz"
buzz_liste = [buz for buz in range(1,101)]
for buz in buzz_liste:
    if buz%3==0 and buz%5==0:
        buzz_liste[buz-1] = "FizzBuzz"
    elif buz%3==0:
        buzz_liste[buz - 1] = "Buzz"
    elif buz%5==0:
        buzz_liste[buz - 1] = "Fizz"
print(buzz_liste)


# Liste aller ersten Buchstaben in einem String
stringa = "Erstelle eine Liste der ersten Buchstaben aller Wörter."
splitta = stringa.split()
first_letters = [wortz[0] for wortz in splitta]
print(first_letters)






