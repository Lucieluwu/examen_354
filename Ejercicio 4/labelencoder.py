import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('./Fortnite_players_stats_no_name.csv')

print("Datos originales:")
print(df.head())

# Crear el LabelEncoder
label_encoder = LabelEncoder()

# Como mi dataset no cuenta con columnas categoricas, esto es solo un ejemplo
for col in df.columns:
    if df[col].dtype == 'object':  # Verifica si la columna es de tipo objeto
        df[col + '_encoded'] = label_encoder.fit_transform(df[col])

print("\nDatos con LabelEncoder aplicado:")
print(df.head())

# Guardar los datos con LabelEncoder en un nuevo archivo CSV
df.to_csv('datos_labelencoded.csv', index=False)
