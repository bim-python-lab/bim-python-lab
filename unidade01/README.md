# Programação Open BIM com Python, (c) PUCRS, 2025

## Unidade 01 - Ambiente de Trabalho

O programa create_walls.py é utilizado para gerar um arquivo IFC mínimo, walls.ifc.

Para testar o ambiente de trabalho, são necessários os arquivos walls.ifc e count_walls.py.

No terminal, basta executar;

```
cd unidade01
python count_walls.py
```

A saída esperada deve ser algo como:
```
Parede A
Parede B
Parede C
```
Caso ocorra um ero, o programa detect_platform.py pode ser utilizado para informar a configuração do ambiente de trabalho.

```
python detect_platform.py
```

A saída normal em abril de 2025, usando o Codespaces seria`

```
Executando no GitHub Codespaces
Plataforma: linux
Python: 3.12.1 (main, Mar 17 2025, 17:13:06) [GCC 9.4.0]
Versão do ifcopenshell: 0.8.1.post1
```

A instalação de bibliotecas no Codespaces e outros ambientes pode ser realizada com os comandos:

```
cd ~
pip install -r requirements.txt
```

Uma configuração de container pode ser utilizada para realizar a instalação das bibliotecas em cada nova máquina virtual.