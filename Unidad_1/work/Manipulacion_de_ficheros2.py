import csv


with open('subvenciones.csv', encoding='utf-8-sig') as fich_lect, \
     open('subvenciones.tsv', 'w', encoding='utf-8-sig', newline='') as fich_escr:
    
    dict_lector = csv.DictReader(fich_lect)
    
    dict_lector.fieldnames = [campo.strip().replace('\ufeff', '') for campo in dict_lector.fieldnames]

    escritor = csv.DictWriter(fich_escr, delimiter='\t', fieldnames=dict_lector.fieldnames)
    escritor.writeheader()
    for linea in dict_lector:
        escritor.writerow(linea)

with open('subvenciones.tsv', encoding='utf-8-sig') as fich:
    dict_lector = csv.DictReader(fich, delimiter='\t')
    
    dict_lector.fieldnames = [campo.strip().replace('\ufeff', '') for campo in dict_lector.fieldnames]

    asocs = {}
    for linea in dict_lector:
        centro = linea['Asociación']
        subvencion = float(linea['Importe'])
        asocs[centro] = asocs.get(centro, 0) + subvencion

print(asocs)
