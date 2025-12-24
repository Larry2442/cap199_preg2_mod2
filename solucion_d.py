import matplotlib.pyplot as plt

df = obtener_datos()

cols = ['age', 'bmi', 'cholesterol_level']
colors = ['orange', 'cyan', 'yellow']

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Boxplots de Variables Numéricas', fontsize=16)

for i, col in enumerate(cols):
    data = df[col].dropna()
    axes[i].boxplot(data, patch_artist=True, boxprops=dict(facecolor=colors[i]))
    axes[i].set_title(f'Boxplot de {col}')
    axes[i].set_xticks([])
    axes[i].set_ylabel('Valores')
    axes[i].grid(True, axis='y', linestyle='-', alpha=0.5)
    axes[i].set_axisbelow(True)

plt.tight_layout()
plt.savefig("grafico_boxplots.png")
print("Boxplots generados.")
plt.show()