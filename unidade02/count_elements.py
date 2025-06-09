# Programação Open BIM com Python, (c) PUCRS, 2025

import ifcopenshell

model = ifcopenshell.open("building_elements.ifc")

types = ["IfcWall", "IfcDoor", "IfcWindow"]

for type in types:
    elems = model.by_type(type)
    print(f"{type}: {len(elems)} encontrados")
    for elem in elems:
        print(" -", elem.Name)