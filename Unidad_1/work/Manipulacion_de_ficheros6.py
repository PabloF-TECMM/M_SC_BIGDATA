import json

with open('subvenciones.json', encoding='utf-8') as fich_lect, \
     open('subvenciones_reformateado.json', 'w', encoding='utf-8') as fich_escr:
    datos = json.load(fich_lect)
    asoc_str = "Asociación"
    act_str = "Actividad Subvencionada"
    imp_str = "Importe en euros"
    lista, list_act = [], []
    asoc_actual, dicc = "", {}
    for elem in datos:
        asoc = elem[asoc_str]
        act = elem[act_str]
        imp = elem[imp_str]
        if asoc_actual != asoc:
            if asoc_actual != "":
                dicc["Actividades"] = list_act
                lista.append(dicc)
            list_act = []
            dicc = {"Asociación": asoc}
        list_act.append({act_str: act, imp_str: imp})
        asoc_actual = asoc
    if dicc and list_act:
        dicc["Actividades"] = list_act
        lista.append(dicc)
    json.dump(lista, fich_escr, ensure_ascii=False, indent=4)