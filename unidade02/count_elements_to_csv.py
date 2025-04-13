import ifcopenshell
import csv

model = ifcopenshell.open("building_elements.ifc")
types = ["IfcWall", "IfcDoor", "IfcWindow"]

with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Tipo", "GlobalId", "Nome"])

    for t in types:
        for elem in model.by_type(t):
            writer.writerow([t, elem.GlobalId, elem.Name])