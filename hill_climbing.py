import random
def objective(x):
    return -(x - 3) ** 2 + 9

def hill_climbing():
    current = random.randint(0, 10)

    print("\nHill Climbing")
    print("Starting Point =", current)

    while True:

        print("\nCurrent =", current)

        neighbors = [current - 1, current + 1]
        neighbors = [n for n in neighbors if 0 <= n <= 10]

        print("Neighbors =", neighbors)

        # Print objective values of neighbors
        for n in neighbors:
            print(f"f({n}) = {objective(n)}")

        best_neighbor = max(neighbors, key=objective)

        print("Best Neighbor =", best_neighbor)

        if objective(best_neighbor) <= objective(current):
            print("No better neighbor found.")
            print("Stopping Hill Climbing...\n")
            break

        print(f"Move: {current} ---> {best_neighbor}")

        current = best_neighbor

    return current, objective(current)



def fitness(chromosome):
    x = int(chromosome, 2)
    return x ** 2

def random_chromosome():
    return ''.join(random.choice('01') for _ in range(5))

def crossover(p1, p2):
    point = random.randint(1, 4)

    print("\nCrossover Point =", point)

    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]

    print("Parent 1 :", p1)
    print("Parent 2 :", p2)
    print("Child 1  :", c1)
    print("Child 2  :", c2)

    return c1, c2

def mutate(chromosome, rate=0.1):

    chrom = list(chromosome)

    print("Before Mutation :", ''.join(chrom))

    for i in range(len(chrom)):
        if random.random() < rate:
            chrom[i] = '1' if chrom[i] == '0' else '0'

    mutated = ''.join(chrom)

    print("After Mutation  :", mutated)

    return mutated

def genetic_algorithm(pop_size=6, generations=20):

    population = [random_chromosome() for _ in range(pop_size)]


    print(" GENETIC ALGORITHM ")
    

    print("\nInitial Population")

    for p in population:
        print(p, " Decimal =", int(p,2), " Fitness =", fitness(p))

    for gen in range(generations):

        
        print("Generation", gen + 1)
        

        population.sort(key=fitness, reverse=True)

        print("\nPopulation after sorting:")

        for p in population:
            print(p, " Decimal =", int(p,2), " Fitness =", fitness(p))

        next_gen = population[:2]

        print("\nElitism (Best 2 kept):")
        print(next_gen)

        while len(next_gen) < pop_size:

            p1, p2 = random.choices(population[:4], k=2)

            print("\nSelected Parents:")
            print("Parent 1 =", p1)
            print("Parent 2 =", p2)

            c1, c2 = crossover(p1, p2)

            c1 = mutate(c1)
            c2 = mutate(c2)

            next_gen.extend([c1, c2])

        population = next_gen[:pop_size]

        print("\nNew Population:")

        for p in population:
            print(p, " Decimal =", int(p,2), " Fitness =", fitness(p))

    best = max(population, key=fitness)

    return best, int(best,2), fitness(best)



if __name__ == "__main__":

    x, val = hill_climbing()

    print("Final Hill Climbing Result")
    print("x =", x)
    print("f(x) =", val)

    chrom, x_val, fit = genetic_algorithm()

    
    print("FINAL GENETIC ALGORITHM RESULT")
    
    print("Best Chromosome =", chrom)
    print("Decimal Value   =", x_val)
    print("Fitness         =", fit)
