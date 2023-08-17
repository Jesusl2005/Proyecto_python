import PySimpleGUI as sg
import tkinter as tk
import pandas as pd

def registro(gastos):

    border_style = {
        "border_width": 2,
        "relief": tk.SOLID
    }

    categorias = ('TRANSPORTE', 'COMIDAS Y BEBIDAS', 'INVERSION', 'VIAJES', 'ELECTRONICA', 'MEDICINA', 'OTROS')

    sg.theme('LightBlue')

    titulos_df = ['id', 'fecha', 'categoria', 'descripcion', 'valor']
    titulos = ['-ID-','-FECHA-', '-CATEGORIA-', '-DESCRIPCION-', '-VALOR-']
    if len(gastos['id']) < 1:
        id = 1
    else:
        id = len(gastos['id']) + 1

    layout = [
        [sg.Text('NUEVO REGISTRO', justification='center', size=(300,1), font=('Courier', 18, 'bold', 'italic'), **border_style)],
        [sg.Text('REGISTRO No', size=(36,1), justification='right', font=('Helvetica', 10, 'bold'), expand_x=True), sg.Input(default_text=id ,key='-ID-', size=(100,1), justification='left', expand_x=True, readonly=True)],
        [sg.Text('FECHA           '), sg.InputText(key='-FECHA-', expand_x=True), sg.CalendarButton("Calendario", target="-FECHA-", format="%d-%m-%Y")],
        [sg.Text('CATEGORIA   '), sg.Combo(values=categorias, expand_x=True, key='-CATEGORIA-', readonly=True)],
        [sg.Text('DESCRIPCION'), sg.Input(key='-DESCRIPCION-', expand_x=True)],
        [sg.Text('VALOR           '), sg.Input(key='-VALOR-', expand_x=True)],
        [sg.Button('GUARDAR',expand_x=True), sg.Button('LIMPIAR', expand_x=True), sg.Button('SALIR', expand_x=True)]
    ]

    window = sg.Window('Nuevo registro', layout, size=(550,220))

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'SALIR':
            guardar(gastos)
            break

        if event == 'GUARDAR':
            dict_values = dict(values)
            dict_values = {clave: valor.upper() for clave, valor in dict_values.items() if clave != 'Calendario'}
            valores = pd.Series(dict_values.values(), titulos_df)
            gastos = pd.concat([gastos, valores.to_frame().T], ignore_index=True)
            for i in titulos:
                if i != '-ID-':
                    window[i].Update('')
            id += 1
            window['-ID-'].update(id)
            window['-FECHA-'].set_focus()
            sg.popup('El registro se ha guardado correctamente', title='Confirmacion')

        if event == 'LIMPIAR':
            for i in titulos:
                if i != '-ID-':
                    window[i].Update('')
            window['-FECHA-'].set_focus()
    window.close()
    return gastos

def guardar(data):
    df = pd.DataFrame(data)
    df.set_index('id', inplace=True)
    df.to_csv('registros_gastos.csv', index=True)