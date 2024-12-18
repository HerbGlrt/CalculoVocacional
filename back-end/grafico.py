import matplotlib.pyplot as plt
import numpy as np

# labels = ["?", "?", "?", "?", "?", "?", "?" ,"?", "?"]
labels = ["Computacao", "Eletrica", "Mecatronica", "Aeronautica", "Licenciatura", "Producao", "Materiais", "Civil", "Ambiental"]
valores = [-21,-5,-17,-8,4,-8,9,23,21]
num_variaveis = len(labels)

angles = np.linspace(0, 2 * np.pi, num_variaveis, endpoint=False).tolist()
valores += valores[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(12 , 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)

ax.set_thetagrids(np.degrees(angles[:-1]), labels, fontsize=14)
ax.set_yticklabels([])

ax.plot(angles, valores, linewidth=3, linestyle='--', color='#04caca')
ax.fill(angles, valores, color='#06fdfd', alpha=0.3)

# Salvar o gráfico
plt.savefig("grafico.png")
