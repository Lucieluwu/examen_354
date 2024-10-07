import pandas as pd

df = pd.read_csv('./Fortnite_players_stats_no_name.csv')

# Inspeccionar las primeras filas
print("Datos originales:")
print(df.head())

# Discretización de todas las columnas
n_bins = 10  # Se podria cambiar el numero de bins según la distribución de los datos
discretized_df = pd.DataFrame()

for col in df.columns:
    # Discretizamos cada columna numérica en 'n_bins' con etiquetas numéricas
    discretized_df[col] = pd.cut(df[col], bins=n_bins, labels=False, include_lowest=True)

print("\nDatos discretizados:")
print(discretized_df.head())

# Guardar los datos discretizados en un nuevo archivo CSV
discretized_df.to_csv('datos_discretizados.csv', index=False)
