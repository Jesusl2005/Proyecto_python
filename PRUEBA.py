import PySimpleGUI as sg
import psycopg2
def guardar(data):
    try:
        conexion = psycopg2.connect(
            host="localhost", database="gastosdb", user="postgres", password="jdlr2005"
        )
        cursor = conexion.cursor()

        for i in range(len(data['-ID-'])):
            id_value = data['-ID-'][i]
            fecha_value = data['-FECHA-'][i]
            categoria_value = data['-CATEGORIA-'][i]
            descripcion_value = data['-DESCRIPCION-'][i]
            valor_value = data['-VALOR-'][i]
            
            cursor.execute(f'INSERT INTO gastos (id, fecha, categoria, descripcion, valor) VALUES ({id_value}, {fecha_value}, {categoria_value}, {descripcion_value}, {valor_value});')
        conexion.commit()
        cursor.close()
        conexion.close()
    except Exception as e:
       #sg.popup(f'{e}', title='Error')
       print(e) 
if __name__ == '__main__':
    registros = {
        '-ID-': ['0','1'],
        '-FECHA-': ['31-07-2023', '31-07-2023'],
        '-CATEGORIA-': ['INVERSION', 'COMIDA Y BEBIDAS'],
        '-DESCRIPCION-': ['PEAJES', 'CENA'],
        '-VALOR-': ['10200', '68000']
    }
    guardar(registros)