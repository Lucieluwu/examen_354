import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def cargar_datos_csv(ruta_archivo, columna_index):
    datos = []
    # Especificar la codificación utf-8
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)  # Omitir la primera fila (encabezados)
        for fila in lector_csv:
            datos.append(float(fila[columna_index]))
    return datos


columna_name = ["Players Name", "Solo score", "Solo top1", "Solo kd", "Solo winRatio", "Solo matches", "Solo kills", "Solo minutesPlayed", "Duos score", "Duos top1", "Duos kd", "Duos winRatio", "Duos matches", "Duos kills",	"Duos minutesPlayed",
                "Trios score", "Trios top1", "Trios kd", "Trios winRatio", "Trios matches", "Trios kills", "Trios minutesPlayed", "Squads score",	"Squads top1", "Squads kd",	"Squads winRatio", "Squads matches", "Squads kills", "Squads minutesPlayed"]

ruta_archivo = './Fortnite_players_stats.csv'

for i in range(1, 4):
    columna_index = i
    datos = cargar_datos_csv(ruta_archivo, columna_index)

    print(columna_name[columna_index])

    media = np.mean(datos)
    print(f"Media: {media}")

    mediana = np.median(datos)
    print(f"Mediana: {mediana}")

    moda = stats.mode(datos)
    print(f"Moda: {moda.mode}")

    plt.figure(figsize=(8, 6))
    sns.boxplot(x=datos, color='skyblue')
    plt.title(f'Diagrama de caja y bigotes - {columna_name[columna_index]}')
    plt.xlabel('Valores')
    plt.show()
