import FreeSimpleGUI as sg

label = sg.Text("inserisci un azione nella to-do list")
inputbox = sg.InputText(tooltip="inserisci un' azione")
button = sg.Button("invia")
# il valore del layout dell'oggetto "Window" richiede un' array di array si oggetti  , quindi ci vanno diverse
# parentesi quadre(minimo 2 paia) , le parentesi quadre servono a mettere o meno gli oggetti
# come il TESTO l' INPUTBOX sulla stessa riga

#in questo caso sono tutti su una riga
window = sg.Window("la mia to-do app", layout=[[label, inputbox, button]])

#mentre per mettere il testo sopa la box verrebbe così:
#window = sg.Window("la mia to-do app", layout=[[label], [inputbox , button]])


#il metodo read dell'oggetto windows permette di visualizzare l'oggetto
window.read()
window.close()