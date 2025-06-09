import ifcopenshell

modelo = ifcopenshell.open("duplex_3D8D.ifc")

def listar_propriedades(elemento):
    if hasattr(elemento, "IsDefinedBy"):
        for rel in elemento.IsDefinedBy:
            if rel.is_a("IfcRelDefinesByProperties"):
                pset = rel.RelatingPropertyDefinition
                if pset.is_a("IfcPropertySet"):
                    print(f"  PSet: {pset.Name}")
                    for prop in pset.HasProperties:
                        print(f"    {prop.Name}: {prop.NominalValue.wrappedValue}")

def consultar_por_tipo(tipo):
    print(f"\n==== {tipo} ====")
    for elem in modelo.by_type(tipo):
        nome = getattr(elem, "Name", "sem nome")
        print(f"\nElemento: {nome}")
        listar_propriedades(elem)

# Consultas por tipo associados às dimensões
consultar_por_tipo("IfcWall")      # 3D, 4D, 6D
consultar_por_tipo("IfcDoor")      # 5D
consultar_por_tipo("IfcSlab")      # 7D
consultar_por_tipo("IfcSpace")     # 8D