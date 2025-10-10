import pandas as pd

with pd.ExcelFile('subvenciones.xls') as xl:
    with pd.ExcelWriter('subvenciones_copia.xls', engine='openpyxl') as escritor:
        for nombre in xl.sheet_names:
            df = xl.parse(nombre)
            df.to_excel(escritor, sheet_name=nombre, index=False)

