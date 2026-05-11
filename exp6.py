import random, math

def f(x, y):
    return math.sin(x) + math.sin(y)

# Initial population
pop = [
    (
        random.uniform(-2 * math.pi, 2 * math.pi),
        random.uniform(-2 * math.pi, 2 * math.pi)
    )
    for _ in range(100)
]

for gen in range(20):
    new_pop = []

    for _ in range(50):
        p1 = random.choice(pop)
        p2 = random.choice(pop)

        # Crossover
        c = (p1[0], p2[1])

        # Mutation
        if random.random() < 0.01:
            c = (
                c[0] + random.uniform(-0.1, 0.1),
                c[1] + random.uniform(-0.1, 0.1)
            )

        new_pop.append(c)

    pop = new_pop

    best = max(pop, key=lambda i: f(i[0], i[1]))
    print(f"Generation {gen+1}: Best individual - {best}, Fitness - {f(best[0], best[1])}")

best = max(pop, key=lambda i: f(i[0], i[1]))
print(f"Best solution found: {best}, Fitness: {f(best[0], best[1])}")
