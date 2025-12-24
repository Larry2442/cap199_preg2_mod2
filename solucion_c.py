# Solucion

import matplotlib.pyplot as plt

df = obtener_datos()

fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Cáncer', fontsize=16, fontweight='bold')

# Distribución de la Edad
axes[0, 0].hist(df['age'].dropna(), bins=5, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Distribución de la edad')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].set_xlabel('Edad')
axes[0, 0].grid(axis='x', alpha=0.5, linestyle='-')
axes[0, 0].grid(axis='y', alpha=0.5, linestyle='-')

# Distribución del género
conteo = df['gender'].value_counts()
axes[0, 1].pie(conteo, labels=conteo.index, autopct='%1.1f%%',startangle=90)
axes[0, 1].set_title('Distribución del género')

# Pacientes por país
df['country'].value_counts().head(27).plot(kind='bar', ax=axes[1, 0], color='salmon')
axes[1, 0].set_title('Pacientes por país')
axes[1, 0].set_ylabel('Cantidad de Pacientes')
axes[1, 0].set_xlabel('País')
axes[1, 0].tick_params(axis='x', rotation=90)

# Distribución de la etapa del cáncer
df['cancer_stage'].value_counts().sort_index().plot(kind='bar', ax=axes[1, 1], color='lightgreen',)
axes[1, 1].set_title('Distribución de la etapa del cáncer')
axes[1, 1].set_ylabel('Cantidad de Pacientes')
axes[1, 1].set_xlabel('Etapa')
axes[1, 1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.savefig("grafico_subplots.png")
print("Subplots generados.")
plt.show()