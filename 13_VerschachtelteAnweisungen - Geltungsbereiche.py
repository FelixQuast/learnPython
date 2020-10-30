# Geltungsbereiche von Variablen

# Beispiel:
x = 25
def drucker():
    x = 50
    print(x)

print(x)
print(drucker())
# Hier ist also x innerhalb der Funktion x=50, während es außerhalb der Funktion x=25 bleibt.
# diese Informationen widersprechen und überschreiben einander nicht
# Die Variablen x=25 und x=50 haben verschiedene Namensreferenzen
#
#   LEGB Regeln
#       Lokal - also zb innerhalb einer Fnktion die man gerade nutzt
#       Einschließe Funktionen - etwa Funktionen innerhalb einer Funktuiooooon
#       Globale (Module) - Variable die innerhalb einer Datei vom Ersteller definiert wird, hier zb x=25
#       Bereits (in Python) eingebaute
#


y = 50

def neuefunktion(y):
    print("y ist gleich ", y)
    y = 2
    print("likaley y ist jetzt aber ", y)

neuefunktion(y)
print("y ist aber gobal noch ", y)

print("marker")

z = 0
def ganzneuefunktion():
    global z
    print("z ist jetzt global ", z)
    z = 100
    print("z wurde jetzt lokal zu ", z)
    print("z wurde aber durch global auch global zu ", z)

print("vor aufruf der ganzneuenfunktion ist z gleich ", z)

ganzneuefunktion()

print("Hier wieder das globale ", z)