import FreeSimpleGUI as sg

label1 = sg.Text("scegli il file da zippare")
inputbox1 = sg.InputText()
#questo è un bottone particolare , permette di selez. files, inserirà in automatico nella inputbox il path dei files
button1 = sg.FileBrowse("Seleziona")

label2 = sg.Text("scegli il file da zippare")
inputbox2 = sg.InputText()
#questo è un bottone particolare , permette di selez. dir, inserirà in automatico nella inputbox il path delle dir
button2 = sg.FolderBrowse("Seleziona")

button3 = sg.Button("Comprimi")
window = sg.Window("File compressor", layout=[[label1, inputbox1, button1], [label2, inputbox2, button2],
                                              [button3]])

window.read()
window.close()