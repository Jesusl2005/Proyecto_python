import PySimpleGUI as sg
import tkinter as tk
import Registrar, Ver, Eliminar
import pandas as pd
import os

def main():

    border_style = {
        "border_width": 2,
        "relief": tk.SOLID
    }

    sg.theme('LightBlue')

    layout = [
        [sg.Text('CONTROL DE GASTOS', justification='center', size=(300,1), font=('Arial', 15, 'bold'), **border_style)],
        [sg.Button('REGISTRAR'), sg.Button('VER'), sg.Button('ELIMINAR'), sg.Button('SALIR')]
    ]

    window = sg.Window('Menu principal', layout, grab_anywhere=True, size=(300,80))

    if os.path.getsize('registros_gastos.csv') == 0:
        registros = pd.DataFrame(columns=['id', 'fecha', 'categoria', 'descripcion', 'valor'], index=[])
    else:
        registros = pd.read_csv('registros_gastos.csv')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'SALIR':
            break

        if event == 'REGISTRAR':
            #Crear modulo registrar
            registros = Registrar.registro(registros)

        if event == 'VER':
            #Crear modulo ver
            Ver.ver(registros)

        if event == 'ELIMINAR':
            #Crear modulo eliminar
            Eliminar.eliminar(registros)

    window.close()
    
if __name__ == '__main__':
    main()