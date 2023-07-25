import PySimpleGUI as sg
from tkinter import *
def main():
    sg.theme('Dark')
    layout = [
        [sg.Text('CONTROL DE GASTOS', justification='center', size=(300,1), font=('Helvetica', 15))],
        [sg.Button('REGISTRAR'), sg.Button('VER'), sg.Button('ELIMINAR'), sg.Button('SALIR')]
    ]

    window = sg.Window('Menu principal', layout, grab_anywhere=True, size=(300,80))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'SALIR':
            break

        if event == 'REGISTRAR':
            #Crear modulo registrar
            break

        if event == 'VER':
            #Crear modulo ver
            break

        if event == 'ELIMINAR':
            #Crear modulo eliminar
            break
    window.close()
if __name__ == '__main__':
    main()