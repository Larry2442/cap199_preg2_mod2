import numpy as np
import matplotlib.pyplot as plt

# Definir datos
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Configurar el gráfico
plt.figure(figsize=(14, 6))
plt.plot(x, y, label='f(x) = sin(x)', color='#555555', linewidth=2.5)

# Datos de las tangentes
datos_tangentes = [
    (0,           "Tangente en x=0",          'red'),
    (np.pi/4,     r"Tangente en x=$\pi$/4",   'green'),
    (np.pi/2,     r"Tangente en x=$\pi$/2",   'blue'),
    (np.pi,       r"Tangente en x=$\pi$",     'm'),
    (3*np.pi/2,   r"Tangente en x=$3\pi$/2",  'c')
]
# Calcular y graficar tangentes
for x0, etiqueta, color in datos_tangentes:
    y0 = np.sin(x0)
    m = np.cos(x0)

    x_linea = np.linspace(x0 - 0.6, x0 + 0.6, 50)
    y_linea = m * (x_linea - x0) + y0

    plt.plot(x_linea, y_linea, '-', color=color, linewidth=2, label=etiqueta)
    
    plt.plot(x0, y0, 'o', color=color, markersize=8)

plt.title("Rectas tangentes a f(x) = sin(x)", fontsize=14, fontweight='bold')
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.ylim(-1.5, 1.5)
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

plt.axhline(0, color='black', linewidth=0.5, alpha=0.3)

plt.savefig("grafico_seno_con_leyenda.png")
plt.show()