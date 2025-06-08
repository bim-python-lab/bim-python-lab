# Programação Open BIM com Python, (c) PUCRS, 2025

import ifcopenshell
import pandas as pd

model = ifcopenshell.open("duplex.ifc")
tipos = ["IfcWall", "IfcDoor", "IfcWindow", "IfcSlab"]
dados = []
for tipo in tipos:
    for elem in model.by_type(tipo):
        dados.append({
            "Tipo": tipo,
            "GlobalId": elem.GlobalId,
            "Nome": getattr(elem, "Name", ""),
            "Tag": getattr(elem, "Tag", "")
        })
df = pd.DataFrame(dados)
print(df.head())
df.to_csv("duplex_dataframe.csv", index=False)