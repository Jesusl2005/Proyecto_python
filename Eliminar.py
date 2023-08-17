import PySimpleGUI as sg
import pandas as pd

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
        if event == sg.WIN_CLOSED or event == 'Salir':
            break
        if event == 'Eliminar':
            try:
                valor = values['valor']
                valor = int(valor) - 1
                
                if valor >= 0 and valor < len(dicts):  # Check if the index is within bounds
                    df_valores = dicts.iloc[valor:valor+1]  # Get a DataFrame row by index
                    layout2 = [
                        [sg.Table(values=df_valores.values.tolist(), headings=list(dicts.columns), display_row_numbers=False,
                                  auto_size_columns=True, num_rows=min(25, len(df_valores)), justification='center',
                                  key='-TABLE-')],
                        [sg.Text('Desea eliminar el registro?', expand_x=True, justification='center')],
                        [sg.Button('Aceptar', expand_x=True), sg.Button('Cancelar', expand_x=True)]
                    ]
                    window2 = sg.Window('Confirmacion', layout2)
                    while True:
                        event2, values2 = window2.read()
                        if event2 == sg.WIN_CLOSED or event2 == 'Cancelar':
                            break
                        if event2 == 'Aceptar':
                            dicts.drop(index=valor, inplace=True)  # Remove row from the DataFrame
                            sg.popup('El registro se ha eliminado correctamente', title='Proceso exitoso')
                            window1['valor'].update('')
                            dicts.set_index('id', inplace=True)
                            dicts.to_csv('registros_gastos.csv', index=True)
                            break
                    window2.close()
                else:
                    sg.popup_error('¡Error! El valor ingresado no es un índice válido.')
            except ValueError:
                sg.popup_error('¡Error! Ingrese un número entero válido.')
    
    window1.close()
