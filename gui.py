import FreeSimpleGUI as sg
import functions

label = sg.Text("inserisci un azione nella to-do list")

inputbox = sg.InputText(tooltip="inserisci un' azione", key="azione")
button = sg.Button("aggiungi")
# il valore del layout dell'oggetto "Window" richiede un' array di array si oggetti  , quindi ci vanno diverse
# parentesi quadre(minimo 2 paia) , le parentesi quadre servono a mettere o meno gli oggetti
# come il TESTO l' INPUTBOX sulla stessa riga

#in questo caso sono tutti su una riga
#window = sg.Window("la mia to-do app", layout=[[label, inputbox, button]], font="Helvetica")

#mentre per mettere il testo sopa la box verrebbe così:

window = sg.Window("la mia to-do app", layout=[[label], [inputbox, button]], font="Helvetica")


#il metodo read dell'oggetto windows permette leggere i valori della finestra , come il bottone e le inputbox ,
#possiamo vedere come ci viene restituito una tupla con una stringa per il valore del bottone , mentre un dizion.
#per il valore della inputbox (dove veng. spec. key e value).
#possiamo predere tutto in una sola variabile ,stamp. perà la tupla per intero: a = window.read()
#print(a)

#oppure valoreizzare correttamente con 2 variabili separate
while True:
    event ,values = window.read()
    print(event)
    print(values)
    match event:
        case "aggiungi":
            todos = functions.get_todos()
            new_todo = values['azione'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            #aggiungiamo un case per quando premiamo la classica "x" per chudere una finestra,
            #questa variabile della libreria è valorizzata a TRUE solo quando premiamo tale bottone.
            break

#una volta usciti dal ciclo potremo chiudere la finestra con window.close
window.close()


