import xlwt

libro_escr = xlwt.Workbook()
asocs = {}
hoja_escr = libro_escr.add_sheet('Totales')

hoja_escr.write(0, 0, "Asociación")
hoja_escr.write(0, 1, "Importe total")
hoja_escr.write(0, 2, "Importe justificado")
hoja_escr.write(0, 3, "Restante")

for i, (asoc, total) in enumerate(asocs.items()):
    fila = i + 1
    hoja_escr.write(fila, 0, asoc)
    hoja_escr.write(fila, 1, total)
    hoja_escr.write(fila, 2, 0)
    formula = f"C{fila+1}-B{fila+1}"
    hoja_escr.write(fila, 3, xlwt.Formula(formula))

libro_escr.save('resumen.xls')