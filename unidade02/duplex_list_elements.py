# Programação Open BIM com Python, (c) PUCRS, 2025

import ifcopenshell
import csv

model = ifcopenshell.open("duplex.ifc")
types = ["IfcWall", "IfcDoor", "IfcWindow", 
          "IfcSlab", "IfcRoof", "IfcStair", "IfcSpace"]

with open("duplex_output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Tipo", "GlobalId", "Nome"])

    for type in types:
        for elem in model.by_type(type):
            name = elem.Name if hasattr(elem, "Name") else ""
            writer.writerow([type, elem.GlobalId, name])