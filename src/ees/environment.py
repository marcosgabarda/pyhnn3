from scipy.stats.distributions import norm

__author__="Marcos Gabarda"
__date__ ="$07-dic-2010 18:47:47$"

class EESEnvironment:
    def __init__(self, data_set, individual, initial_population=10, \
    generations=100):
        self.__population = []
        self.__parents = []
        self.__offspring = []
        self.__data_set = data_set
        self.__individual = individual
        self.__initial_population = initial_population
        self.__id_count = 0
        self.__generations = generations
        if self.__data_set.mode == "cls":
            self.__problem = "max"
        else:
            self.__problem = "min"
        self.__selection_mode = "ml"

    def __initialize(self):
        for i in range(self.__initial_population):
            ind = object.__new__(self.__individual)
            ind.__init__( self.__data_set , i)
            ind.update_score()
            print ind
            self.__population.append(ind)
        self.__id_count = self.__initial_population

    def __selection(self):
        # Select all the population to be parents
        self.__parents = []
        for i in range(len(self.__population)):
            self.__parents.append(self.__population[i])

    def __mutation(self, factor=7):
        self.__offspring = []
        offspring_star = norm.rvs(loc=factor*len(self.__parents))
        total_fitness = 0.0
        for i in range(len(self.__parents)):
            total_fitness += self.__parents[i].score
        for i in range(len(self.__parents)):
            p = self.__parents[i]
            offspring_factor = offspring_star * (p.score / total_fitness)
            for j in range(int(offspring_factor)):
                self.__id_count += 1
                o = p.mutate()
                o.id = self.__id_count
                o.update_score()
                self.__offspring.append(o)

    def __replacement(self, mode="ml"):
        self.__population = []
        individuals = []
        if mode == "ml":
            for i in range(len(self.__offspring)):
                individuals.append((self.__offspring[i].score, self.__offspring[i]))
        else:
            individuals = []
            for i in range(len(self.__offspring)):
                individuals.append((self.__offspring[i].score, self.__offspring[i]))
            for i in range(len(self.__parents)):
                individuals.append((self.__parents[i].score, self.__parents[i]))
        if self.__problem == "max":
            individuals = sorted(individuals, key=lambda ind: ind[0], reverse=True)
        else:
            individuals = sorted(individuals, key=lambda ind: ind[0])
        for i in range(len(self.__parents)):
            self.__population.append(individuals[i][1])
        self.__parents = []
        self.__offspring = []


    def __evolutionary_cycle(self):
        print "--- Selection..."
        self.__selection()
        print "--- Mutation..."
        self.__mutation()
        print "--- Replacement..."
        self.__replacement(mode=self.__selection_mode)

    def get_best(self):
        individuals = []
        if self.__problem == "max":
            individuals = sorted(self.__population, key=lambda ind: ind.score,\
            reverse=True)
        else:
            individuals = sorted(self.__population, key=lambda ind: ind.score)
        return individuals[0]

    def run(self):
        print "--- Initial population ---"
        self.__initialize()
        current_generation = 0
        while current_generation < self.__generations:
            current_generation += 1
            print "Generation " + str(current_generation)
            self.__evolutionary_cycle()
            best = self.get_best()
            print "Best: " + str(best)
            print "(Parent ID: " +  str(best.parent.id) + ")"
            

if __name__ == "__main__":
    pass