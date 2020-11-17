# The Primo Insurance Company is introducing two new product lines: special risk insurance and mortgages. The expected profit is $5 per unit on special risk insurance and $2 per unit on mortgages. Management wishes to establish sales quotas for the new product lines to maximize total expected profit. The work requirements are as follows:

# Department	Special Risk	Mortgage	Work-Hours Available
#
# Underwriting	           3           2                    2400
# Administration           0           1                     800
# Claims                   2           0                    1200

# Objective: Maximize Z = 5 * x[0] + 2 * x[1] 
#
# Subject to:
#
# 3 * x[0] + 2 * x[1] <= 2400
#            1 * x[1] <=  800
# 2 * x[0]            <= 1200
#
# Solution: x[0] == 600; x[1] == 300

import random
from matplotlib import pyplot as plt

def is_viable(x):
    if 3 * x[0] + 2 * x[1] <= 2400:
        pass
    else:
        return False

    if x[1] <= 800:
        pass
    else:
        return False
    
    if 2 * x[0] <= 1200:
        pass
    else:
        return False
    
    return True


def evaluate(x):
    return 5 * x[0] + 2 * x[1]


n = 50 # population size

population = [] # individuals
best_x = None # best fit individual
best_z = 0 # evaluation of the best individual

# creating the first population
while len(population) < n:
    x = [random.randint(0, 1000), random.randint(0, 1000)]

    if is_viable(x):
        population.append(x)
        z = evaluate(x)
        if z > best_z:
            best_z = z
            best_x = x

zs = [] # evaluation through the generations

generations = 5000 # number of populations
for generation in range(generations):
    new_generation = []
    while len(new_generation) < n:
        # crossover
        temp = population.copy()
        parent_1 = random.choice(temp)
        temp.remove(parent_1) 
        parent_2 = random.choice(population)
        new_x = [parent_1[0], parent_2[1]]

        # mutation
        if random.random() > 0.8:
            gene = random.choice([0, 1])
            new_x[gene] = random.randint(0, 1000)
        
        if is_viable(new_x):
            new_generation.append(new_x)
            z = evaluate(new_x)
            if z > best_z:
                best_z = z
                best_x = new_x
    population = new_generation.copy()
    zs.append(best_z)

print(generation, best_x, best_z)
plt.plot(zs);
plt.show()