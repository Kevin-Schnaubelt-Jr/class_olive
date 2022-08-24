# Mob Programming: Jackalope Simulator
# Version 1
# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

# Jackalopes are reproductive from ages 4-8 and die at age 10.
# Gestation is instantaneous. Each gestation produces two offspring.
# Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
# With these conditions in mind, we can represent our population as a list of ints.

jackalopes = [0, 0]

population = len(jackalopes)

# print(jackalopes)

year = 0
while len(jackalopes) <= 1000:        
    year += 1
    bachelopes = 0

    for index, value in enumerate(jackalopes):
        # age all jackalopes one year
        jackalopes[index] += 1
        
    for index, value in enumerate(jackalopes):
        # If 2 jackalopes are between 4-8, add 2 to population
        if jackalopes[index] >= 4 and jackalopes[index] <= 8:
            bachelopes += 1
                    
    if bachelopes % 2 == 0 and bachelopes != 0:
        jackalopes.append(0)
        jackalopes.append(0)
    print(bachelopes % 2)      # wonky
    # print(jackalopes)

print(year) # years it took to get 1000 jackalopes

# TO DO
# Handle deaths
# Figure out modulus