import random

def objective_function(x):
    try:
        # Calcula el valor de la función
        result = x**(2*x) - 1
        # Filtramos numeros reales
        return result.real if isinstance(result, complex) else result
    except (ValueError, TypeError):
        # En caso de error, retornamos un número muy grande
        return float('inf')


def initialize_population(size, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(size)]

# Evaluamos la población


def evaluate_population(population):
    return [objective_function(individual) for individual in population]

# Selección de padres


def select_parents(population, fitness):
    real_population = [ind for ind, fit in zip(
        population, fitness) if fit != float('inf')]
    real_fitness = [fit for fit in fitness if fit != float('inf')]

    if not real_population:  # Si no hay individuos reales, volvemos a inicializar
        return random.choices(population, k=2)

    total_fitness = sum(real_fitness)
    probabilities = [f / total_fitness for f in real_fitness]
    return random.choices(real_population, weights=probabilities, k=2)

# Cruce (crossover)


def crossover(parent1, parent2):
    alpha = random.random()
    return alpha * parent1 + (1 - alpha) * parent2

# Mutación


def mutate(individual, mutation_rate, lower_bound, upper_bound):
    if random.random() < mutation_rate:
        return random.uniform(lower_bound, upper_bound)
    return individual

# Algoritmo Genético


def genetic_algorithm(population_size, generations, mutation_rate, lower_bound, upper_bound):
    population = initialize_population(
        population_size, lower_bound, upper_bound)

    for generation in range(generations):
        fitness = evaluate_population(population)
        print(
            f"Generación {generation + 1}: Población: {population}, Fitness: {fitness}")

        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population, fitness)
            offspring = crossover(parent1, parent2)
            offspring = mutate(offspring, mutation_rate,
                               lower_bound, upper_bound)
            new_population.append(offspring)

        population = new_population

    # Evaluar la última generación
    fitness = evaluate_population(population)
    best_individual = population[fitness.index(min(fitness))]
    return best_individual, objective_function(best_individual)


# Parámetros
population_size = 10  # Tamaño de la población
generations = 3       # Número de generaciones
mutation_rate = 0.1   # Tasa de mutación
lower_bound = -10     # Límite inferior del rango
upper_bound = 10      # Límite superior del rango

best_solution, best_value = genetic_algorithm(
    population_size, generations, mutation_rate, lower_bound, upper_bound)

print(
    f"La mejor solución encontrada es: x = {best_solution}, con valor f(x) = {best_value}")
