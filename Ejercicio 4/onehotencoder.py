import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('./Fortnite_players_stats_no_name.csv')

# Inspeccionar las primeras filas
print("Datos originales:")
print(df.head())

# Crear el OneHotEncoder
onehot_encoder = OneHotEncoder(sparse=False)

# Como mi dataset no cuenta con columnas categoricas, esto es solo un ejemplo
for col in df.columns:
    if df[col].dtype == 'object':  # Verifica si la columna es de tipo objeto
        encoded_data = onehot_encoder.fit_transform(df[[col]])
        # Convertir a DataFrame y concatenar con el original
        onehot_df = pd.DataFrame(encoded_data, columns=onehot_encoder.get_feature_names_out([col]))
        df = pd.concat([df, onehot_df], axis=1).drop(columns=[col])  # Eliminar la columna original

print("\nDatos con OneHotEncoder aplicado:")
print(df.head())

# Guardar los datos con OneHotEncoder en un nuevo archivo CSV
df.to_csv('datos_onehotencoded.csv', index=False)
