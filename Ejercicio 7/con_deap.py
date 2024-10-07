import random
from deap import base, creator, tools

def objective_function(x):
    try:
        result = x**(2*x) - 1
        return (result.real,)  # Devolver un tuple con el valor real
    except (ValueError, TypeError):
        return (float('inf'),)  # Retornar infinito si hay un error


# Crear las clases de evaluación y optimización
creator.create("FitnessMin", base.Fitness,
               weights=(-1.0,))  # Minimizar la función
creator.create("Individual", list, fitness=creator.FitnessMin)

# Inicializar el toolbox
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -10, 10)  # Rango de valores
toolbox.register("individual", tools.initRepeat,
                 creator.Individual, toolbox.attr_float, n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", lambda ind: objective_function(
    ind[0]))  # Evaluar el primer (y único) elemento
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Algoritmo Genético


def genetic_algorithm(population_size, generations):
    population = toolbox.population(n=population_size)

    for generation in range(generations):
        # Evaluar la población
        fitnesses = list(map(toolbox.evaluate, population))
        for ind, fit in zip(population, fitnesses):
            ind.fitness.values = fit

        print(
            f"Generación {generation + 1}: Población: {[ind[0] for ind in population]}, Fitness: {fitnesses}")

        # Seleccionar padres
        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        # Aplicar cruce y mutación
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < 0.5:  # Probabilidad de cruce
                toolbox.mate(child1, child2)
                del child1.fitness.values  # Forzar a recalcular la aptitud
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < 0.2:  # Probabilidad de mutación
                toolbox.mutate(mutant)
                del mutant.fitness.values  # Forzar a recalcular la aptitud

        # Actualizar la población
        population[:] = offspring

    # Evaluar la última generación
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    # Encontrar la mejor solución
    fits = [ind.fitness.values[0] for ind in population]
    best_index = fits.index(min(fits))
    best_individual = population[best_index]
    return best_individual, best_individual.fitness.values[0]


# Parámetros
population_size = 10  # Tamaño de la población
generations = 3       # Número de generaciones

best_solution, best_value = genetic_algorithm(population_size, generations)

print(
    f"La mejor solución encontrada es: x = {best_solution[0]}, con valor f(x) = {best_value}")
