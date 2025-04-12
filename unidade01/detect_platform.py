# Programação Open BIM com Python, (c) PUCRS, 2025

# Verificar se estamos no Google Colab
try:
    import google.colab
    print("Executando no Google Colab")
except ImportError:
    pass

# Verificar se estamos no Codespaces
import os
if "CODESPACES" in os.environ:
    print("Executando no GitHub Codespaces")

# Verificar se estamos em um notebook
try:
    shell = get_ipython().__class__.__name__
    if shell == 'ZMQInteractiveShell':
        print("Executando em Jupyter Notebook local")
except NameError:
    pass

# Verificar em qual sistema operacional estamos
import sys
print("Plataforma:", sys.platform)

# Verificar a versão de Python
print("Python:", sys.version)

# Verificar a versão do IFC
try:
    import ifcopenshell
    print("Versão do ifcopenshell:", ifcopenshell.__version__)
except Exception:
    print("ICF não está disponível")