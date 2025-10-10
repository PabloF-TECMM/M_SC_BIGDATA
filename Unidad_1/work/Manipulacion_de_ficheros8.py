import xml.etree.ElementTree as ET

# Datos simulando el contenido de subvenciones
asocs = {
    "AMPA ANTONIO MACHADO": [
        {"Actividad": "TALLER FIESTA DE CARNAVAL", "Importe": 94.56},
        {"Actividad": "TALLER DIA DEL PADRE", "Importe": 39.04}
    ]
}

# Crear el árbol y la raíz
nuevo = ET.ElementTree()
raiz_nueva = ET.Element("Raiz")
nuevo._setroot(raiz_nueva)

# Recorrer asociaciones
for centro, actividades_lista in asocs.items():
    # Crear elemento <Asociacion> con atributo nombre
    elem_actual = ET.SubElement(raiz_nueva, "Asociacion")
    elem_actual.set("nombre", centro)

    # Crear elemento <Actividades>
    actividades = ET.SubElement(elem_actual, "Actividades")

    total = 0
    # Recorrer actividades
    for act in actividades_lista:
        act_elem = ET.SubElement(actividades, "Actividad")
        act_elem.set("nombre", act["Actividad"])
        importe_elem = ET.SubElement(act_elem, "Importe")
        importe_elem.text = str(act["Importe"])
        total += act["Importe"]

    # Agregar total al final
    gas_total = ET.SubElement(elem_actual, "Total")
    gas_total.text = str(round(total, 2))

# Guardar el XML en un archivo
nuevo.write("subvenciones_reorganizado.xml", encoding="utf-8", xml_declaration=True)