import ifcopenshell
import sys

if len(sys.argv) != 2:
    print("Uso: python query_walls.py <arquivo.ifc>")
    sys.exit(1)

arquivo = sys.argv[1]
modelo = ifcopenshell.open(arquivo)

def exibir_estrutura(elemento):
    nome = getattr(elemento, "Name", "sem nome")
    print(f"{elemento.is_a()} – {nome}")
    if hasattr(elemento, "IsDefinedBy"):
        for rel in elemento.IsDefinedBy:
            if rel.is_a("IfcRelDefinesByProperties"):
                pset = rel.RelatingPropertyDefinition
                if pset.is_a("IfcPropertySet"):
                    print(f"  └── PropertySet: {pset.Name}")
                    for prop in pset.HasProperties:
                        valor = getattr(prop.NominalValue, "wrappedValue", prop.NominalValue)
                        print(f"      └── {prop.Name}: {valor}")

# Exibe a estrutura do primeiro IfcWall
paredes = modelo.by_type("IfcWall")
if paredes:
    exibir_estrutura(paredes[0])
else:
    print("Nenhuma parede encontrada.")