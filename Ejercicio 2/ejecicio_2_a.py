import csv
import matplotlib.pyplot as plt

# Función para cargar los datos desde un archivo CSV


def cargar_datos_csv(ruta_archivo, columna_index):
    datos = []
    # Especificar la codificación utf-8
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)  # Omitir la primera fila (encabezados)
        for fila in lector_csv:
            datos.append(float(fila[columna_index]))
    return datos

# Función para calcular un percentil


def calcular_percentil(datos, percentil):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    k = (n - 1) * (percentil / 100)
    f = int(k)
    c = k - f

    if f + 1 < n:
        return datos_ordenados[f] + (c * (datos_ordenados[f + 1] - datos_ordenados[f]))
    else:
        return datos_ordenados[f]

# Función para calcular los cuartiles


def calcular_cuartiles(datos):
    q1 = calcular_percentil(datos, 25)
    q2 = calcular_percentil(datos, 50)
    q3 = calcular_percentil(datos, 75)
    return q1, q2, q3

# Función para graficar el histograma de una columna de datos


def graficar_histograma(datos, nombre_columna):
    plt.hist(datos, bins=10, edgecolor='black', alpha=0.7)
    plt.title(f'Histograma de {nombre_columna}')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()


# Cargar datos desde el archivo CSV
ruta_archivo = './Fortnite_players_stats.csv'
columna_name = ["Players Name", "Solo score", "Solo top1", "Solo kd", "Solo winRatio", "Solo matches", "Solo kills", "Solo minutesPlayed", "Duos score", "Duos top1", "Duos kd", "Duos winRatio", "Duos matches", "Duos kills",	"Duos minutesPlayed",
                "Trios score", "Trios top1", "Trios kd", "Trios winRatio", "Trios matches", "Trios kills", "Trios minutesPlayed", "Squads score",	"Squads top1", "Squads kd",	"Squads winRatio", "Squads matches", "Squads kills", "Squads minutesPlayed"]

for i in range(1, 29):
# for i in range(1, 3):
    columna_index = i  # Índice de la columna de interés
    datos = cargar_datos_csv(ruta_archivo, columna_index)

    print(columna_name[columna_index])
    # Calcular cuartiles
    q1, q2, q3 = calcular_cuartiles(datos)
    print(f"Cuartil 1 (Q1): {q1}")
    print(f"Cuartil 2 (Q2) o mediana: {q2}")
    print(f"Cuartil 3 (Q3): {q3}")

    # Calcular un percentil específico, por ejemplo, el percentil 90
    p90 = calcular_percentil(datos, 90)
    print(f"Percentil 90: {p90}")

    graficar_histograma(datos, columna_name[columna_index])
