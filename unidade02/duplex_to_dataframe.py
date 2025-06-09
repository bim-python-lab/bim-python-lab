# Programação Open BIM com Python, (c) PUCRS, 2025

import ifcopenshell
import pandas as pd

model = ifcopenshell.open("duplex.ifc")
types = ["IfcWall", "IfcDoor", "IfcWindow", "IfcSlab"]
data = []
for type in types:
    for elem in model.by_type(type):
        data.append({
            "Typo": type,
            "GlobalId": elem.GlobalId,
            "Name": getattr(elem, "Name", ""),
            "Tag": getattr(elem, "Tag", "")
        })
df = pd.DataFrame(data)
print(df.head())
df.to_csv("duplex_dataframe.csv", index=False)