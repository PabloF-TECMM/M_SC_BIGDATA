import xlrd

libro = xlrd.open_workbook('subvenciones.xls')
asocs = {}

for hoja in libro.sheets():
    for i in range(1, hoja.nrows):  
        fila = hoja.row(i)
        asoc = fila[0].value        
        subvencion = float(fila[2].value)  
        asocs[asoc] = asocs.get(asoc, 0) + subvencion

print(asocs)
