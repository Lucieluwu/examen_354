import csv

def read_csv(filename):
    data = []
    with open(filename, newline='',  encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data.append([float(value) for value in row])
    return data

def normalize(data):
    normalized_data = []
    for i in range(len(data[0])):  # Para cada columna
        column = [row[i] for row in data]
        min_val = min(column)
        max_val = max(column)
        normalized_col = [(value - min_val) / (max_val - min_val)
                          for value in column]
        normalized_data.append(normalized_col)
    return list(map(list, zip(*normalized_data)))  # Transponer la lista

# Calcular la penalización L1


def l1_penalty(weights):
    return sum(abs(w) for w in weights)

# Calcular la penalización L2


def l2_penalty(weights):
    return sum(w ** 2 for w in weights)

# Función principal


def main():
    filename = './Fortnite_players_stats_no_name.csv'
    data = read_csv(filename)

    # Normalizar los datos
    normalized_data = normalize(data)

    weights = [0.1, 0.2, 0.3]

    # Calcular penalizaciones
    l1 = l1_penalty(weights)
    l2 = l2_penalty(weights)

    print("L1 Penalty:", l1)
    print("L2 Penalty:", l2)


if __name__ == "__main__":
    main()
