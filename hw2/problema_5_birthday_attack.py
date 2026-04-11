import math
import numpy as np
import matplotlib.pyplot as plt

def simulacion_cumpleanos(n_espacio=100000):
    d_vals = np.arange(1, 2500)

    # Formula de la probabilidad de colision
    probabilidades = 1 - np.exp(-(d_vals * (d_vals - 1)) / (2 * n_espacio))

    # Punto de inflexion (probabilidad muy cercana a 1, ej. 0.999)
    # d = sqrt(-2n * ln(1 - P))
    d_inflexion = math.sqrt(-2 * n_espacio * math.log(1 - 0.999))
    print(f"Mensajes para colision inminente (>99.9%): {math.ceil(d_inflexion)}")

    plt.figure(figsize=(9,5))
    plt.plot(d_vals, probabilidades, label="Probabilidad simulada")
    plt.axvline(d_inflexion, color='red', linestyle='--', label=f"Inflexion d={math.ceil(d_inflexion)}")

    plt.title("Birthday Attack Simulado en RSA")
    plt.xlabel("Numero de mensajes interceptados (d)")
    plt.ylabel("Probabilidad de colision")
    plt.grid(True)
    plt.legend()
    plt.show()

simulacion_cumpleanos()
