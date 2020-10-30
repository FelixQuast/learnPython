# Lambda Operator
#  Lambda-Funktionen kommen aus der funktionalen Programmierung. Mit Hilfe des lambda-Operators können
#  anonyme Funktionen, d.h. Funktionen ohne Namen erzeugt werden. Sie haben eine beliebe Anzahl von
#  Parametern, führen einen Ausdruck aus und liefern den Wert dieses Ausdrucks als Rückgabewert zurück.
#
# Anonyme Funktionen sind insbesondere bei der Anwendung der map-, filter- und reduce-Funktionen von großem Vorteil.


# BEISPIEL aus udemy
square = lambda zahl: zahl**2

# Anwendung der neu definierten Square() funktion
print(square(3))


even = lambda x: x%2 ==0
print("Even von 2, 3 und 4:")
print(even(2))
print(even(5))
print(even(4))



# EIGENES BEISPIEL, Summe dreier Zahlen
summe_dreierlei = lambda a,b,c: a+b+c

print(summe_dreierlei(2,3,5))

