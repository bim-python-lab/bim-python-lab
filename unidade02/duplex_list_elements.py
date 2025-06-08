# Programação Open BIM com Python, (c) PUCRS, 2025

import ifcopenshell
import csv

model = ifcopenshell.open("duplex.ifc")
tipos = ["IfcWall", "IfcDoor", "IfcWindow", 
          "IfcSlab", "IfcRoof", "IfcStair", "IfcSpace"]

with open("duplex_output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Tipo", "GlobalId", "Nome"])

    for tipo in tipos:
        for elem in model.by_type(tipo):
            nome = elem.Name if hasattr(elem, "Name") else ""
            writer.writerow([tipo, elem.GlobalId, nome])