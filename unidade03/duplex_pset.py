import ifcopenshell
from ifcopenshell.api import run

# ---------- Função de filtragem reutilizável ----------

def filter(model, type=None, named=None):
    for elem in model.by_type(type) if type else model:
        if named and named.lower() not in getattr(elem, "Name", "").lower():
            continue
        yield elem

# ---------- Função de atualização reutilizável ----------

def add_prop(model, pset, name, value):
    if isinstance(value, str):
        value = model.create_entity("IfcText", value)
    elif isinstance(value, (int, float)):
        value = model.create_entity("IfcReal", float(value))
    prop = model.create_entity("IfcPropertySingleValue", Name=name,
                               NominalValue=value, Unit=None)
    if pset.HasProperties is None:
        pset.HasProperties = [prop]
    else:
        pset.HasProperties.append(prop)


# ---------- Carrega modelo ----------
model = ifcopenshell.open("duplex.ifc")

# ---------- 3D: Contagem de elementos ----------
walls = list(filter(model, type="IfcWall"))
print("Paredes:", len(walls))

# ---------- 4D: Etapas construtivas ----------
for wall in walls:
    phase = "Alvenaria Externa" if "exterior" in wall.Name.lower() else "Alvenaria Interna"
    pset = run("pset.add_pset", model, product=wall, name="PSet_Tarefa4D")
    add_prop(model, pset, "EtapaConstrutiva", phase)
    print(f"Valor {phase} adicionado à parede {wall.Name}")

# ---------- 5D: Custo das portas ----------
for door in filter(model, type="IfcDoor"):
    value = 1800 if "dupla" in getattr(door, "Name", "").lower() else 1200
    pset = run("pset.add_pset", model, product=door, name="PSet_Custo5D")
    add_prop(model, pset, "CustoUnitario", value)
    print(f"Valor {value} adicionada à porta {door.Name}")

# ---------- 6D: Classe energética das paredes ----------
for wall in walls:
    ec = "B" if "exterior" in getattr(wall, "Name", "").lower() else "A"
    pset = run("pset.add_pset", model, product=wall, name="PSet_Energia6D")
    add_prop(model, pset, "ClasseEnergetica", ec)
    print(f"Valor {ec} adicionada à parede {wall.Name}")

# ---------- 7D: Datas de manutenção em lajes ----------
for slab in filter(model, type="IfcSlab"):
    pset = run("pset.add_pset", model, product=slab, name="PSet_Manutencao7D")   
    deadline = "2026-01-01"
    add_prop(model, pset, "RevisaoPrevista", deadline)
    print(f"Valor {deadline} adicionada ao piso {slab.Name}")

# ---------- 8D: Zonas de risco em ambientes ----------
for space in filter(model, type="IfcSpace"):
    pset = run("pset.add_pset", model, product=space, name="PSet_Seguranca8D")
    risk = "Risco de Queda" if "A105" in getattr(space, "Name", "").upper() else "Área Geral"
    add_prop(model, pset, "ZonaDeRisco", risk)
    print(f"Valor {risk} adicionada ao espaço {space.Name}")

# ---------- Salva resultado ----------
model.write("duplex_3D8D.ifc")
print("Arquivo salvo: Duplex_3D8D.ifc")