import random

def f(x):
    return -x**2 + 6*x + 9

# Initial population
pop = [random.uniform(-10, 10) for _ in range(50)]

for gen in range(50):
    new_pop = []

    for _ in range(50):
        p1 = random.choice(pop)
        p2 = random.choice(pop)

        # Crossover
        c = (p1 + p2) / 2

        # Mutation
        if random.random() < 0.01:
            c += random.uniform(-1, 1)

        new_pop.append(c)

    pop = new_pop

    best = max(pop, key=f)
    print(f"Generation {gen+1}: Best individual - {best}, Fitness - {f(best)}")

best = max(pop, key=f)
print(f"Best solution found: {best}, Fitness: {f(best)}")
