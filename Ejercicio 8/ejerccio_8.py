import pandas as pd
import numpy as np
import math

df = pd.read_csv('./dataset.csv')

def entropy(column):
    elements, counts = np.unique(column, return_counts=True)
    entropy = 0
    for count in counts:
        probability = count / len(column)
        entropy -= probability * math.log2(probability)
    return entropy

entropia_inicial = entropy(df['obesidad'])
print(f'Entropía inicial (obesidad): {entropia_inicial}')

def info_gain(data, split_attribute, target_attribute):
    # Entropía inicial de la clase objetivo
    total_entropy = entropy(data[target_attribute])

    # Valores únicos del atributo por el que se va a dividir
    vals, counts = np.unique(data[split_attribute], return_counts=True)

    weighted_entropy = 0
    for i in range(len(vals)):
        subset = data[data[split_attribute] == vals[i]]
        subset_entropy = entropy(subset[target_attribute])
        weighted_entropy += (counts[i] / sum(counts)) * subset_entropy

    # Ganancia de información
    information_gain = total_entropy - weighted_entropy
    return information_gain

ganancia_peso = info_gain(df, 'peso', 'obesidad')
print(f'Ganancia de información por el atributo "peso": {ganancia_peso}')

ganancia_talla = info_gain(df, 'talla', 'obesidad')
print(f'Ganancia de información por el atributo "talla": {ganancia_talla}')

ganancia_altura = info_gain(df, 'altura', 'obesidad')
print(f'Ganancia de información por el atributo "altura": {ganancia_altura}')

