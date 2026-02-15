import numpy as np
import pandas as pd
from parar import gerar_seed_global, monte_carlo
from time import perf_counter
from os import urandom

'''
resultados[i][i][i]
           |  |  |  
   pontuação  |  |
      resultado  |
      carta do dealer
'''
maos = (
    "4H", "5H", "6H", "7H", "8H", "9H", "10H", "11H", "12H", "13H", "14H", "15H", "16H", "17H", "18H", "19H", "20H",
    "12S", "13S", "14S", "15S", "16S", "17S", "18S", "19S", "20S", "21S"
)
carta = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'A')
estats = [0 for _ in range(27)]
resultados = np.array([
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)]),
    np.array([np.zeros(10, dtype=int), np.zeros(10, dtype=int), np.zeros(10, dtype=int)])
], dtype=int)

gerar_seed_global(int.from_bytes(urandom(4), "big"))

t0 = perf_counter()
print(monte_carlo(resultados, 100_000_000, 0, 0))
t = perf_counter() - t0

vitorias = resultados[:, 0, :]
derrotas = resultados[:, 1, :]
empates = resultados[:, 2, :]
df_vitorias = pd.DataFrame(vitorias, index=maos, columns=carta)
df_derrotas = pd.DataFrame(derrotas, index=maos, columns=carta)
df_empates = pd.DataFrame(empates, index=maos, columns=carta)
df_estats = pd.DataFrame(estats)

with pd.ExcelWriter("MelhorEstrat.xlsx") as writer:
    df_vitorias.to_excel(writer, sheet_name="Pedir, Dobrar ou Parar", startcol=1, startrow=1)
    df_derrotas.to_excel(writer, sheet_name="Pedir, Dobrar ou Parar", startcol=13, startrow=1)
    df_empates.to_excel(writer, sheet_name="Pedir, Dobrar ou Parar", startcol=25, startrow=1)
    df_estats.to_excel(writer, sheet_name="Pedir, Dobrar ou Parar", startcol=37, startrow=1)

print(t)