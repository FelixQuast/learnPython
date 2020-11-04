# TicTacToe Spiel Programmieren
# 1.    Hauptproblem: Wie arbeite ich überhaupt mit soetwas iwe einem Spielfeld, also etwas
#       was der Spieler sehen kann?
#
# 2:    Wie mache ich Eingaben mit der Maus?
# NOTES:
# Spieler 1: X
# Spieler 2: O
from tkinter import *
from functools import partial
import ast

# Counter etc.
spieler_eins = True
l1 = [0,0,0]
l2 = [0,0,0]
l3 = [0,0,0]
matrix = [l1,
          l2,
          l3]

#matrix = [l1,l2,l3]


# Funktionen
def button_action():
    anweisungs_label.config(text="Ich wurde geändert!")

def pick(ident, matrix_ident):
    global spieler_eins
    global matrix
    button_state = eval(ident).cget('text')
    if spieler_eins == True:
        if button_state != " ":
            return
        spieler_eins = False
        matrix_ident = matrix_ident.replace("spaceship","1")
        eval(ident).config(text="X")    # Feld markieren X
        exec(matrix_ident)
    elif spieler_eins == False:
        if button_state != " ":
            return
        spieler_eins = True
        matrix_ident = matrix_ident.replace("spaceship","2")
        eval(ident).config(text="O")    # Feld markieren O
        exec(matrix_ident)
    print(matrix)
    print("\n",
          l1, "\n",
          l2, "\n",
          l3)
    spalte1 = [l1[0],l2[0],l3[0]]
    spalte2 = [l1[1],l2[1],l3[1]]
    spalte3 = [l1[2],l2[2],l3[2]]
    gewinner()


def winner_one():
    print("Spieler 1 hat gewonnen")

def winner_two():
    print("Spieler 2 hat gewonnen")

def gewinner():
    print("test")
    for zeile in matrix:
        print("Hier ist Zeile: " , zeile)
    if zeile[0] == zeile[1] == zeile[2] == 1:
        winner_one()
    elif zeile[0] == zeile[1] == zeile[2] == 2:
        winner_two()





    # Fenster für GUI mit tkinter

fenster = Tk()
fenster.geometry("500x700")
fenster.title("TicTacToe")


# Buttons:
change_button = Button(fenster, text="änder mich", command=button_action)
exit_button = Button(fenster, text="BEENDEN", command=fenster.quit)
B_aa = Button(fenster, text =" ", command=partial(pick, "B_aa", "matrix[0][0] = spaceship"))
B_ab = Button(fenster, text =" ", command=partial(pick, "B_ab", "matrix[0][1] = spaceship"))
B_ac = Button(fenster, text =" ", command=partial(pick, "B_ac", "matrix[0][2] = spaceship"))

B_ba = Button(fenster, text =" ", command=partial(pick, "B_ba", "matrix[1][0] = spaceship"))
B_bb = Button(fenster, text =" ", command=partial(pick, "B_bb", "matrix[1][1] = spaceship"))
B_bc = Button(fenster, text =" ", command=partial(pick, "B_bc", "matrix[1][2] = spaceship"))

B_ca = Button(fenster, text =" ", command=partial(pick, "B_ca", "matrix[2][0] = spaceship"))
B_cb = Button(fenster, text =" ", command=partial(pick, "B_cb", "matrix[2][1] = spaceship"))
B_cc = Button(fenster, text =" ", command=partial(pick, "B_cc", "matrix[2][2] = spaceship"))


# LABELS
anweisungs_label = Label(fenster, text="Ich bin eine Anweisung:\n\
Klicke auf 'Ändern'.")
info_label = Label(fenster, text="TicTacToe\n\
Spieler 1 ist X, Spieler 2 ist O")


#BUTTON-PLACEMENT
#anweisungs_label.place(x = 0, y = 0, width=200, height=150)
#change_button.place(x = 220, y = 0, width=200, height=150)
info_label.place(x = 175, y = 20, width=150, height=40)
exit_button.place(x = 200, y = 570, width=100, height=50)

B_aa.place(x =  80, y = 200, width=100, height=100)
B_ab.place(x = 200, y = 200, width=100, height=100)
B_ac.place(x = 320, y = 200, width=100, height=100)

B_ba.place(x =  80, y = 320, width=100, height=100)
B_bb.place(x = 200, y = 320, width=100, height=100)
B_bc.place(x = 320, y = 320, width=100, height=100)

B_ca.place(x =  80, y = 440, width=100, height=100)
B_cb.place(x = 200, y = 440, width=100, height=100)
B_cc.place(x = 320, y = 440, width=100, height=100)



# Durch die GUI handelt es sich um ereignisbasiertes Programmieren.
# Wir müssen also eine Endlosschleife programmieren aus der herausgestartet wird sobald
#   eine Eingabe erfolgt
fenster.mainloop()