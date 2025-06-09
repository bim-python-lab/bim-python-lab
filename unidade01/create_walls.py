# Programação Open BIM com Python, (c) PUCRS, 2025
# TESTE

import ifcopenshell
import ifcopenshell.api

# Criar novo arquivo IFC
ifc = ifcopenshell.api.run("project.create_file")

# Criar entidades principais
project = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcProject", name="Projeto Simples")
context = ifcopenshell.api.run("context.add_context", ifc, context_type="Model")
site = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcSite", name="Terreno")
building = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcBuilding", name="Pr\u00e9dio")
storey = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcBuildingStorey", name="Pavimento 1")

# Estabelecer hierarquia correta
ifcopenshell.api.run("aggregate.assign_object", ifc, relating_object=project, products=[site])
ifcopenshell.api.run("aggregate.assign_object", ifc, relating_object=site, products=[building])
ifcopenshell.api.run("aggregate.assign_object", ifc, relating_object=building, products=[storey])

# Criar 3 paredes simples e atribuí-las ao pavimento
for name in ["Parede A", "Parede B", "Parede C"]:
    wall = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcWallStandardCase", name=name)
    ifcopenshell.api.run("spatial.assign_container", ifc, relating_structure=storey, products=[wall])

# Salvar arquivo IFC
ifc.write("walls.ifc")
print("Arquivo IFC 'modelo_tres_paredes.ifc' gerado com sucesso!")
