# Programação Open BIM com Python, (c) PUCRS, 2025

import ifcopenshell

model = ifcopenshell.open("building_elements.ifc")

types = ["IfcWall", "IfcDoor", "IfcWindow"]

for tipo in types:
    elementos = model.by_type(tipo)
    print(f"{tipo}: {len(elementos)} encontrados")
    for elem in elementos:
        print(" -", elem.Name)