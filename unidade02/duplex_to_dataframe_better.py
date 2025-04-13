import ifcopenshell
import pandas as pd

model = ifcopenshell.open("duplex.ifc")
tipos = ["IfcWall", "IfcDoor", "IfcWindow"]
# generator  
dados = (
    {
        "Tipo": tipo,
        "GlobalId": elem.GlobalId,
        "Nome": getattr(elem, "Name", ""),
        "Tag": getattr(elem, "Tag", "")
    }
    for tipo in tipos
    for elem in model.by_type(tipo)
)
df = pd.DataFrame.from_records(dados)
print(df.head())
df.to_csv("duplex_dataframe_better.csv", index=False)