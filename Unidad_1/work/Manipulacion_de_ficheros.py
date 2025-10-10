import csv

with open('subvenciones.csv', encoding='utf-8-sig') as fichero_csv:
    dict_lector = csv.DictReader(fichero_csv)

    # Mostrar encabezados detectados
    print("Encabezados originales:", dict_lector.fieldnames)

    # Limpiar encabezados (quita espacios y BOM)
    dict_lector.fieldnames = [
        campo.strip().replace('\ufeff', '') for campo in dict_lector.fieldnames
    ]
    print("Encabezados limpios:", dict_lector.fieldnames)

    asocs = {}
    for linea in dict_lector:
        centro = linea['Asociación']
        subvencion = float(linea['Importe'])
        asocs[centro] = asocs.get(centro, 0) + subvencion

    print(asocs)

with open('subvenciones.csv', encoding='latin1') as fich_lect, \
     open('subvenciones_esc.csv', 'w', encoding='latin1') as fich_escr:
    dict_lector = csv.DictReader(fich_lect)
    campos = dict_lector.fieldnames + ['Justificación requerida', 'Justificación recibida']
    escritor = csv.DictWriter(fich_escr, fieldnames=campos)
    escritor.writeheader()
    for linea in dict_lector:
        linea['Justificación requerida'] = "Sí" if float(linea['Importe']) > 300 else "No"
        linea['Justificación recibida'] = "No"
        escritor.writerow(linea)
