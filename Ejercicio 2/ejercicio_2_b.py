import csv
import matplotlib.pyplot as plt

def cargar_datos_csv(ruta_archivo, columna_index):
    datos = []
    # Especificar la codificación utf-8
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)  # Omitir la primera fila (encabezados)
        for fila in lector_csv:
            datos.append(float(fila[columna_index]))
    return datos

ruta_archivo = './Fortnite_players_stats.csv'
columna_name = ["Players Name", "Solo score", "Solo top1", "Solo kd", "Solo winRatio", "Solo matches", "Solo kills", "Solo minutesPlayed", "Duos score", "Duos top1", "Duos kd", "Duos winRatio", "Duos matches", "Duos kills",	"Duos minutesPlayed",
                "Trios score", "Trios top1", "Trios kd", "Trios winRatio", "Trios matches", "Trios kills", "Trios minutesPlayed", "Squads score",	"Squads top1", "Squads kd",	"Squads winRatio", "Squads matches", "Squads kills", "Squads minutesPlayed"]

solo_winrate = cargar_datos_csv(ruta_archivo, 4)
solo_timeplayed = cargar_datos_csv(ruta_archivo, 7)
solo_kd = cargar_datos_csv(ruta_archivo, 3)


# Crear el gráfico de dispersión
plt.figure(figsize=(10, 8))
scatter = plt.scatter(solo_timeplayed, solo_kd, c=solo_winrate, s=100, cmap='viridis', alpha=0.7)

# Añadir barra de color
cbar = plt.colorbar(scatter)
cbar.set_label('Win Rate en Solo')

# Etiquetas de los ejes
plt.xlabel('Tiempo Jugado (min)')
plt.ylabel('K/D en Solo')
plt.title('Gráfico de Dispersión: Tiempo Jugado vs K/D en Solo')
plt.show()
