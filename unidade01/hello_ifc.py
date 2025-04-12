# Programação Open BIM com Python, (c) PUCRS, 2025

import sys
import ifcopenshell

print("Plataforma:", sys.platform)
print("Python:", sys.version)
print("Versão do ifcopenshell:", ifcopenshell.__version__)

print("Abrindo o arquivo de exemplo com modelo de três paredes:")

model = ifcopenshell.open("modelo_tres_paredes.ifc")
print("Entidades com GlobalId:", len(model.by_type("IfcRoot")))
print("Entidades:", model.schema)