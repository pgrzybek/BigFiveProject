import pandas as pd
import numpy as np

# 🔹 1. Wpisz swoje dane (lista wyników surowych)
wyniki = [12, 18, 21, 15, 23, 28, 14, 19, 17, 26, 20, 22, 13, 25, 16, 24, 27, 29, 30]

# 🔹 2. Oblicz średnią i odchylenie standardowe
M = np.mean(wyniki)
SD = np.std(wyniki, ddof=1)

# 🔹 3. Oblicz z-score i steny
z_scores = [(x - M) / SD for x in wyniki]
steny = [round(z * 2 + 5.5) for z in z_scores]

# 🔹 4. Ogranicz wartości do 1–10
steny = [min(max(s, 1), 10) for s in steny]

# 🔹 5. Utwórz tabelę
df = pd.DataFrame({
    'Wynik surowy': wyniki,
    'Z-score': np.round(z_scores, 2),
    'Sten': steny
})

# 🔹 6. Posortuj po wyniku surowym
df = df.sort_values('Wynik surowy').reset_index(drop=True)

print("Średnia:", round(M, 2))
print("Odchylenie standardowe:", round(SD, 2))
print("\nTabela przeliczeniowa (wynik → sten):")
print(df)
