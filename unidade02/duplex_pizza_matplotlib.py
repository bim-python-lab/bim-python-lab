# Programação Open BIM com Python, (c) PUCRS, 2025

import ifcopenshell
from collections import Counter
import matplotlib.pyplot as plt

model = ifcopenshell.open("duplex.ifc")
types = [e.is_a() for e in model if hasattr(e, "Name")]
counts = Counter(types)
top = counts.most_common(4)
labels = [item[0] for item in top]
data = [item[1] for item in top]

plt.pie(data, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Distribuição dos tipos no modelo Duplex")
plt.axis("equal")
plt.savefig("pizzaplt")
plt.show()