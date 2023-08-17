import PySimpleGUI as sg
import pandas as pd

def eliminar(dicts: pd.DataFrame):
    sg.theme('LightBlue')
    layout = [
        [sg.Text('Eliminar registro No.', justification='center', expand_x=True), sg.Input(key='valor', justification='left', expand_x=True)],
        [sg.Button('Eliminar', expand_x=True), sg.Button('Salir', expand_x=True)]
    ]

    window1 = sg.Window('Eliminar registro', layout)
    while True:
        event, values = window1.read()
        if event == 'Eliminar':
            try:
                valor = values['valor']
                valor = int(valor) - 1
                valores = dicts[valor]
                df_valores = pd.DataFrame(valores)
                layout2 = [
                    [sg.Table(values=df_valores.values.tolist(), headings=list(dicts.keys()), display_row_numbers=False,
                            auto_size_columns=True, num_rows=min(25, len(dicts)), justification='center',
                            key='-TABLE-')],
                    [sg.Text('Desea eliminar el registro?', expand_x=True, justification='center')],
                    [sg.Button('Aceptar', expand_x=True), sg.Button('Cancelar', expand_x=True)]
                ]
                window2 = sg.Window('Confirmacion', layout2)
                while True:
                    event, values = window2.read()
                    if event == 'Aceptar':
                        dict.drop(values['valor'])
                        sg.popup('El registro se ha eliminado correctamente', title='Proceso exitoso')
                    if event == 'Cancelar' or event == sg.WIN_CLOSED:
                        break
                window2.close()
            except ValueError:
                sg.popup_error('¡Error! Ingrese un número entero válido.')
        if event == 'Salir' or event == sg.WIN_CLOSED:
            break
    window1.close()
