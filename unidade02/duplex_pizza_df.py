# Programação Open BIM com Python, (c) PUCRS, 2025

import pandas as pd
import matplotlib.pyplot as plt

# Supondo que df foi gerado anteriormente
df = pd.read_csv("duplex_dataframe.csv")

counts = df["Tipo"].value_counts().head(4)
counts.plot.pie(autopct='%1.1f%%', startangle=90)

plt.title("Distribuição dos tipos no modelo Duplex")
plt.ylabel("")
plt.savefig("pizzadf")
plt.show()