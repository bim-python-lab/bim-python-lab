import ifcopenshell
import sys

if len(sys.argv) != 2:
    print("Uso: python query_walls.py <arquivo.ifc>")
    sys.exit(1)

file = sys.argv[1]
model = ifcopenshell.open(file)

def display(elem):
    name = getattr(elem, "Name", "*")
    print(f"{elem.is_a()} – {name}")
    if hasattr(elem, "IsDefinedBy"):
        for rel in elem.IsDefinedBy:
            if rel.is_a("IfcRelDefinesByProperties"):
                pset = rel.RelatingPropertyDefinition
                if pset.is_a("IfcPropertySet"):
                    print(f"  └── PropertySet: {pset.Name}")
                    for prop in pset.HasProperties:
                        value = getattr(prop.NominalValue, "wrappedValue", prop.NominalValue)
                        print(f"      └── {prop.Name}: {value}")

# Exibe a estrutura do primeiro IfcWall
walls = model.by_type("IfcWall")
if walls:
    display(walls[0])
else:
    print("Nenhuma parede encontrada.")