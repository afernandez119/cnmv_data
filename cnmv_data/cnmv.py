import fitz
import re
import pandas as pd

def get_portfolio(path_pdf):
    '''
    Devuelve una lista de listas que contiene la tabla reportada en PDF por el Fondo de Inversion (FI)
    sin encabezados.
    Se utiliza el formato estandarizado exigido por la CNVM que básicamente solicita 6 campos en la tabla:
        - ISIN + Nombre de la empresa
        - Divisa
        - Valor de mercado actual
        - % sobre el total del fondo actual
        - Valor de mercado del pasado trimestre
        - % sobre el total del fondo del último trimestre
    
    Se puede convertir directamente en un DataFrame:
        - pd.DataFrame(result, columns = ['ISIN','Nombre', 'Divisa', 'Actual_VM', 'Actual_%', 'Pasado_VM', 'Pasado_%'])

    Parameters:
        path_pdf (str):Ruta del fichero PDF del cual queremos extraer la informacion.

    Returns:
        result (list of list):Lista de listas con la información sobre la cartera del FI.

    Example:
        [['US0082521081 - ACCIONES|Affiliated Managers Group', 'USD', '2.071', '0,80', '0', '0,00'],
        ['FR0011476928 - ACCIONES|Fnac Darty SA', 'EUR', '222', '0,09', '0', '0,00'],
        ['US5006881065 - ACCIONES|Kosmos Energy LTD', 'USD', '3.145', '1,22', '4.726', '1,05'],
        ['IT0005252140 - ACCIONES|Saipem SPA', 'EUR', '2.631', '1,02', '5.321', '1,18']]
    '''

    with fitz.open(path_pdf) as document:
        text = ''
        for page in document:
            text += page.getText()

    text = text.replace('�','')

    lines = text.split('\n')

    index_stocks = [1 if re.match(r'^\w{2}\d{9}', line) else 0 for line in lines]

    index_stocks = [i for i, s in enumerate(index_stocks) if s==1 in index_stocks]

    result = []

    for i in index_stocks:
        stock = lines[i:i+6]
        result.append([p.strip() for p in stock])
    
    return (result)
