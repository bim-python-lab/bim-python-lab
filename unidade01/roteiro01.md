# Roteiro da Unidade 1 – Ambiente de Trabalho para Programação Open BIM

Este documento oferece os roteiros e links necessários para configurar o ambiente de desenvolvimento e executar o primeiro script da disciplina.

---

## Arquivos do Curso

- [count_walls.py](https://raw.githubusercontent.com/bim-python-lab/bim-python-lab/refs/heads/main/unidade01/count_walls.py)
- [walls.ifc](https://raw.githubusercontent.com/bim-python-lab/bim-python-lab/refs/heads/main/unidade01/walls.ifc)

> Substitua `seu-usuario` pela sua conta ou organização GitHub real.

---

## Instalação do Python (Windows, macOS, Linux)

- Site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Após instalar, verifique no terminal:
```bash
python --version
```

---

## Visual Studio Code (VS Code)

- Download: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Extensões recomendadas:
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

### Passos:
```bash
mkdir openbim-projeto && cd openbim-projeto
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install ifcopenshell pandas
```

---

## GitHub Codespaces

- Acesso: [https://github.com/features/codespaces](https://github.com/features/codespaces)

### Pré-requisitos:
- Instalar bibliotecas manualmente com:
```
pip install ifcopenshell pandas
```

Ou

- Repositório com `requirements.txt` e `.devcontainer/devcontainer.json` contendo:
```json
{
  "name": "Python BIM",
  "image": "mcr.microsoft.com/devcontainers/python:3.10",
  "postCreateCommand": "pip install -r requirements.txt"
}
```

### Passos:
- Clique em "Code" → "Open with Codespaces" → "Create codespace"

---

## Google Colab

- Acesso: [https://colab.research.google.com](https://colab.research.google.com)

### Passos:
1. Criar novo notebook
2. Executar:
```python
!pip install ifcopenshell pandas
```
3. Fazer upload de `walls.ifc`
4. Executar os comandos do script count_walls.py

---

## Jupyter Notebook Local

- Instale via Anaconda ou pip:
```bash
pip install jupyterlab ifcopenshell pandas
```
- Execute:
```bash
jupyter notebook
```

---

## Relatando problemas

Ao relatar um erro no ambiente virtual de aprendizagem, inclua:
- Ambiente: Colab, Codespaces, VS Code, Jupyter local
- Sistema operacional (Windows/macOS/Linux)
- Código ou trecho executado
- Mensagem de erro completa
- Captura de tela

### Atalhos para captura de tela:
- Windows: `Windows + Shift + S`
- macOS: `Command + Shift + 4`
- Linux: `Print Screen` ou `Shift + Print Screen`
