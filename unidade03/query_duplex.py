import ifcopenshell

modelo = ifcopenshell.open("duplex_3D8D.ifc")

def list_prop(elem):
    if hasattr(elem, "IsDefinedBy"):
        for rel in elem.IsDefinedBy:
            if rel.is_a("IfcRelDefinesByProperties"):
                pset = rel.RelatingPropertyDefinition
                if pset.is_a("IfcPropertySet"):
                    print(f"  PSet: {pset.Name}")
                    for prop in pset.HasProperties:
                        print(f"    {prop.Name}: {prop.NominalValue.wrappedValue}")

def query_by(type):
    print(f"\n==== {type} ====")
    for elem in modelo.by_type(type):
        nome = getattr(elem, "Name", "sem nome")
        print(f"\nElemento: {nome}")
        list_prop(elem)

# Consultas por tipo associados às dimensões
query_by("IfcWall")      # 3D, 4D, 6D
query_by("IfcDoor")      # 5D
query_by("IfcSlab")      # 7D
query_by("IfcSpace")     # 8D