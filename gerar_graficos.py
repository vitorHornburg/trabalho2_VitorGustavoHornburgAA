
import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("resultados_teste_casos_completo.csv")

os.makedirs("graficos", exist_ok=True)

casos = df["Caso"].unique()
for caso in casos:
    plt.figure(figsize=(10, 6))
    df_caso = df[df["Caso"] == caso]
    for algoritmo in df_caso["Algoritmo"].unique():
        df_alg = df_caso[df_caso["Algoritmo"] == algoritmo]
        plt.plot(df_alg["Tamanho"], df_alg["Tempo Médio (s)"], marker='o', label=algoritmo)
    plt.title(f"Tempo Médio - Caso {caso}")
    plt.xlabel("Tamanho do Vetor")
    plt.ylabel("Tempo Médio (s)")
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    nome_arquivo = f"graficos/grafico_{caso.lower()}.png"
    plt.savefig(nome_arquivo)
    print(f"Gráfico salvo: {nome_arquivo}")
