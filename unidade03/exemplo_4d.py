import ifcopenshell
from ifcopenshell.api import run

# ---------- Função de filtragem reutilizável ----------

def filtrar(model, tipo=None, nome_contendo=None):
    for elem in model.by_type(tipo) if tipo else model:
        if nome_contendo and nome_contendo.lower() not in getattr(elem, "Name", "").lower():
            continue
        yield elem

# ---------- Função de atualização reutilizável ----------

def adicionar_propriedade(model, pset, nome, valor):
    if isinstance(valor, str):
        valor = model.create_entity("IfcText", valor)
    elif isinstance(valor, (int, float)):
        valor = model.create_entity("IfcReal", float(valor))
    prop = model.create_entity("IfcPropertySingleValue", Name=nome,
                               NominalValue=valor, Unit=None)
    if pset.HasProperties is None:
        pset.HasProperties = [prop]
    else:
        pset.HasProperties.append(prop)


# ---------- Carrega modelo ----------
model = ifcopenshell.open("duplex.ifc")

# ---------- 3D: Contagem de elementos ----------
walls = list(filtrar(model, tipo="IfcWall"))
print("Paredes:", len(walls))

# ---------- 4D: Etapas construtivas ----------
for wall in walls:
    etapa = "Alvenaria Externa" if "externa" in wall.Name.lower() else "Alvenaria Interna"
    pset = run("pset.add_pset", model, product=wall, name="PSet_Tarefa4D")
    adicionar_propriedade(model, pset, "EtapaConstrutiva", etapa)
    print(f"Valor {etapa} adicionado à parede {wall.Name}")

# ---------- 5D: Custo das portas ----------
for door in filtrar(model, tipo="IfcDoor"):
    preco = 1800 if "dupla" in getattr(door, "Name", "").lower() else 1200
    pset = run("pset.add_pset", model, product=door, name="PSet_Custo5D")
    adicionar_propriedade(model, pset, "CustoUnitario", preco)
    print(f"Valor {preco} adicionada à porta")

# ---------- 6D: Classe energética das paredes ----------
for wall in walls:
    classe = "B" if "externa" in getattr(wall, "Name", "").lower() else "A"
    pset = run("pset.add_pset", model, product=wall, name="PSet_Energia6D")
    adicionar_propriedade(model, pset, "ClasseEnergetica", classe)
    print(f"Valor {classe} adicionada à parede {wall.Name}")


# ---------- Salva resultado ----------
model.write("duplex_3D8D.ifc")
print("Arquivo salvo: Duplex_3D8D.ifc")