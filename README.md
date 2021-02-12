# CNMV Portfolio extraction

![](https://files.catbox.moe/4b74gp.jpg)

```https://pypi.org/project/cnmv-data/1.0.0/```
<br>

Librería que te permite extraer las carteras reportadas por los Fondos de Inversión
de manera trimestrar a la CNMV en formato PDF.

Para utilizarlo simplemente necesitas disponer de un fichero PDF del FI en el que se incluya la cartera
y siga el formato exigido por la CNMV.
Básicamente la tabla reportada incluye los siguientes datos:

    - ISIN + Nombre de la empresa
    - Divisa
    - Valor de mercado actual
    - % sobre el total del fondo actual
    - Valor de mercado del pasado trimestre
    - % sobre el total del fondo del último trimestre



Por Antonio Fernández Troyano
<br>


## 💡 Prerequisitos

   [Python 3](https://www.python.org/downloads/release/python-370/)

<br>


## 🛠️ Instalación:

### Con PyPI
```pip3 install cnmv_data```

<br>


## 📚 Ejemplo de uso

```
from cnmv_data import get_portfolio

get_portfolio('.\Q1.pdf')
```
<br>


## 💥 Output
```
    [['US0082521081 - ACCIONES|Affiliated Managers Group', 'USD', '2.071', '0,80', '0', '0,00'],
    ['FR0011476928 - ACCIONES|Fnac Darty SA', 'EUR', '222', '0,09', '0', '0,00'],
    ['US5006881065 - ACCIONES|Kosmos Energy LTD', 'USD', '3.145', '1,22', '4.726', '1,05'],
    ['IT0005252140 - ACCIONES|Saipem SPA', 'EUR', '2.631', '1,02', '5.321', '1,18']]
```

Se puede convertir directamente en un DataFrame:
```
pd.DataFrame(result, columns = ['ISIN + Nombre', 'Divisa', 'Actual_VM', 'Actual_%', 'Pasado_VM', Pasado_%'])
```
|ISIN + Nombre |Divisa|Actual_VM|Actual_%|Pasado_VM|Pasado_%|
|--------------|------|---------|--------|---------|--------|
|US0082521081 - ACCIONES Affiliated Managers Group|USD|2.071| 0,80| 0| 0,00|
|FR0011476928 - ACCIONES Fnac Darty SA| EUR| 222| 0,09| 0| 0,00|
|US5006881065 - ACCIONES Kosmos Energy LTD| USD| 3.145| 1,22| 4.726| 1,05|
|IT0005252140 - ACCIONES Saipem SPA| EUR| 2.631| 1,02| 5.321| 1,18|
<br><br>


## 🐸 Aloha!
<br>

![https://www.linkedin.com/in/atroyano/](https://files.catbox.moe/t62e9k.png)