class Hund(object):
    spezies = "Säugetier"
    def __init__(self,rasse,name):
        self.rasse = rasse
        self.name = name




sam = Hund(rasse="Labrador", name="Sam")
frank = Hund(rasse="Husky", name="Frank")

print("Die Klasse von 'Hund' ist: ", type(Hund))

print(frank.rasse)
print(sam.spezies)
print(sam.name)