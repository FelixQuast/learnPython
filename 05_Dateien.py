# Dateien
import os


print (os.getcwd())

textfile = open("uebung.txt", "w+")

print("Das ist eine Textdatei", file=textfile)

a = textfile.read()

print(a)



