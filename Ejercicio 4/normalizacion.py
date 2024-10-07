import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('./Fortnite_players_stats_no_name.csv')

# Inspeccionar las primeras filas
print("Datos originales:")
print(df.head())

# Normalización de todas las columnas
scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print("\nDatos normalizados:")
print(df_normalized.head())

# Guardar los datos normalizados en un nuevo archivo CSV
df_normalized.to_csv('datos_normalizados.csv', index=False)
