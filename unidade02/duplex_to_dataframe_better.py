# Programação Open BIM com Python, (c) PUCRS, 2025

import ifcopenshell
import pandas as pd

model = ifcopenshell.open("duplex.ifc")
types = ["IfcWall", "IfcDoor", "IfcWindow", "IfcSlab"]
# generator - less memory required
data = (
    {
        "Type": type,
        "GlobalId": elem.GlobalId,
        "Name": getattr(elem, "Name", ""),
        "Tag": getattr(elem, "Tag", "")
    }
    for type in types
    for elem in model.by_type(tipo)
)
df = pd.DataFrame.from_records(data)
print(df.head())
df.to_csv("duplex_dataframe_better.csv", index=False)