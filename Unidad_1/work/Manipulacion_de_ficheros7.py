import xml.etree.ElementTree as ET

arbol = ET.parse('subvenciones.xml')
raiz = arbol.getroot()
asocs = {}
for fila in raiz.findall('Row'):
    centro = fila.find('Asociaci_n').text
    subvencion = float(fila.find('Importe').text)
    asocs[centro] = asocs.get(centro, 0) + subvencion
print(asocs)