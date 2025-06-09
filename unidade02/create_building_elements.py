# Programação Open BIM com Python, (c) PUCRS, 2025

import ifcopenshell
import ifcopenshell.api

# Criar novo arquivo IFC
ifc = ifcopenshell.api.run("project.create_file")

# Criar estrutura do projeto
project = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcProject", name="Projeto Exemplo")
context = ifcopenshell.api.run("context.add_context", ifc, context_type="Model")
site = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcSite", name="Terreno")
building = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcBuilding", name="Prédio")
storey = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcBuildingStorey", name="Pavimento 1")

# Hierarquia
ifcopenshell.api.run("aggregate.assign_object", ifc, relating_object=project, products=[site])
ifcopenshell.api.run("aggregate.assign_object", ifc, relating_object=site, products=[building])
ifcopenshell.api.run("aggregate.assign_object", ifc, relating_object=building, products=[storey])

# Adicionar elementos
for name in ["Parede A", "Parede B", "Parede C"]:
    wall = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcWallStandardCase", name=name)
    ifcopenshell.api.run("spatial.assign_container", ifc, relating_structure=storey, products=[wall])

for name in ["Porta 1", "Porta 2"]:
    door = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcDoor", name=name)
    ifcopenshell.api.run("spatial.assign_container", ifc, relating_structure=storey, products=[door])

window = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcWindow", name="Janela 1")
ifcopenshell.api.run("spatial.assign_container", ifc, relating_structure=storey, products=[window])

# Salvar arquivo
ifc.write("building_elements.ifc")
print("Arquivo IFC gerado com sucesso.")