import FreeSimpleGUI as sg
import functions

label = sg.Text("inserisci un azione nella to-do list")

inputbox = sg.InputText(tooltip="inserisci un' azione", key="todo")
button = sg.Button("aggiungi")
# il valore del layout dell'oggetto "Window" richiede un' array di array si oggetti  , quindi ci vanno diverse
# parentesi quadre(minimo 2 paia) , le parentesi quadre servono a mettere o meno gli oggetti
# come il TESTO l' INPUTBOX sulla stessa riga

#in questo caso sono tutti su una riga
#window = sg.Window("la mia to-do app", layout=[[label, inputbox, button]], font="Helvetica")

#mentre per mettere il testo sopa la box verrebbe così:

listbox = sg.Listbox(values=functions.get_todos(), enable_events=True, key="todos", size=[45, 10])

button_list = sg.Button("edit")

window = sg.Window("la mia to-do app", layout=[[label], [inputbox, button],
                                               [listbox, button_list]], font="Helvetica")


#il metodo read dell'oggetto windows permette leggere i valori della finestra , come il bottone e le inputbox ,
#possiamo vedere come ci viene restituito una tupla con una stringa per il valore del bottone , mentre un dizion.
#per il valore della inputbox (dove veng. spec. key e value).
#possiamo predere tutto in una sola variabile ,stamp. perà la tupla per intero: a = window.read()
#print(a)

#oppure valorizzare correttamente con 2 variabili separate
while True:
    event ,values = window.read()
    print(event)
    print(values)
    match event:
        case "aggiungi":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos) #aggiorniamo la lista un avolta agg. nuovi items
        case sg.WIN_CLOSED:
            #aggiungiamo un case per quando premiamo la classica "x" per chudere una finestra,
            #questa variabile della libreria è valorizzata a TRUE solo quando premiamo tale bottone.
            break
        case "edit":
            todo_to_edit = values["todos"] [0]
            #todo è la chiave della prima inputbox, quindi scegliamo un valore nella listbox e lo sost.
            #con quello nella inputbox
            new_todo = values["todo"] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            #facciamo l'update della lista in gui a real-time , aggiornando il valore dell'oggetto windows
            window['todos'].update(values=todos)
            #con window[todos]indichiamo l'istanza della windows che ha come
            #chiave il valore "todos" , nel nostro caso è la listbox a riga 17.

        case "todos":
            # qui aggiorniamo il campo della inputbox quando clicchiamo un items della list , in modo che
            #compaia il testo selezionato
            window['todo'].update(value=values['todos'][0])




#una volta usciti dal ciclo potremo chiudere la finestra con window.close
window.close()


