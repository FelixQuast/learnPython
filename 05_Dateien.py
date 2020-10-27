# Dateien
import os


print (os.getcwd())

textfile = open("uebung.txt", "w+")

print("Das ist eine Textdatei", file=textfile)
textfile.seek(0)
a = textfile.read()
print(a)
textfile.close()

x = open("text.txt", "w")
print("This is my file", file = x)
x.close()