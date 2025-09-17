import pandas as pd
import matplotlib.pyplot as plt

# Ler CSV com médias geradas pelo main.py
df = pd.read_csv("resultados_resumo.csv")

# Filtrar apenas tempo e potência, pegar médias
tempos = df[df["Métrica"]=="tempo"][["Algoritmo", "Média"]].set_index("Algoritmo")
potencias = df[df["Métrica"]=="potencia"][["Algoritmo", "Média"]].set_index("Algoritmo")

# Garantir mesma ordem
nomes = tempos.index
tempos_medios = tempos["Média"].values
potencias_medias = potencias["Média"].values

# Criar gráfico scatter
plt.figure(figsize=(10,6))
plt.scatter(tempos_medios, potencias_medias, color='green', s=100)

# Adicionar rótulos dos algoritmos
for i, nome in enumerate(nomes):
    plt.text(tempos_medios[i]*1.01, potencias_medias[i]*1.01, nome, fontsize=9)

plt.xlabel("Tempo médio (s)")
plt.ylabel("Potência média (W)")
plt.title("Comparação Tempo x Potência dos Algoritmos")
plt.grid(True)
plt.tight_layout()
plt.savefig("tempo_vs_potencia.png")
# plt.show()
