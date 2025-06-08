import ifcopenshell
from collections import Counter
import matplotlib.pyplot as plt

model = ifcopenshell.open("duplex.ifc")
tipos = [e.is_a() for e in model if hasattr(e, "Name")]
contagem = Counter(tipos)
mais_comuns = contagem.most_common(4)
labels = [item[0] for item in mais_comuns]
valores = [item[1] for item in mais_comuns]

plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Distribuição dos tipos no modelo Duplex")
plt.axis("equal")
plt.savefig("pizzaplt")
plt.show()