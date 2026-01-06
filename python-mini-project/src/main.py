import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
df = pd.read_csv("../Data.csv")

# Colonnes MTF
mtf_cols = [col for col in df.columns if col.startswith("MTF")]


print(" INFORMATIONS GÉNÉRALES")
print("Nombre de lignes :", len(df))
print("\nStatistiques sur Z :")
print(df["Z"].describe())

print("\nStatistiques sur les MTF (moyenne) :")
print(df[mtf_cols].mean())

print("\nStatistiques sur les MTF (min / max) :")
print(df[mtf_cols].agg(["min", "max"]))

plt.figure(figsize=(10, 6))

for col in mtf_cols:
    plt.plot(df["Z"], df[col], label=col)

plt.xlabel("Z")
plt.ylabel("MTF")
plt.title("Évolution des MTF en fonction de Z")
plt.legend()
plt.grid(True)
plt.show()
