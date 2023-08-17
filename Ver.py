import PySimpleGUI as sg
import pandas as pd
def ver(dict: pd.DataFrame):
    
    layout = [
        [sg.Table(values=dict.values.tolist(), headings=list(dict.keys()), display_row_numbers=False,
                  auto_size_columns=True, num_rows=min(25, len(dict)), justification='center',
                  enable_click_events=True, key='-TABLE-')],
        [sg.Button('OK', size=(10,1))]
    ]

    window = sg.Window('Registros', layout, element_justification='center')
    
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'OK':
            break
    window.close()