# Programação Open BIM com Python, (c) PUCRS, 2025

import ifcopenshell

model = ifcopenshell.open("walls.ifc")
for wall in model.by_type("IfcWall"):
    print(wall.Name)