import math

from scipy.stats.distributions import norm
from scipy.stats.distributions import randint
from scipy.stats.distributions import uniform

__author__="Marcos Gabarda"
__date__ ="$07-dic-2010 15:39:08$"

class Section:
    def __init__(self, label, individual, size, linf=None, lsup=None):
        self.individual = individual
        self.genes = []
        self.lsup = lsup
        self.linf = linf
        self.size = size
        self.label = label
        self.tau = 1.0 / math.sqrt(2.0 * math.sqrt(size))
        self.tau_prim = 1.0 / math.sqrt(2.0 * size);

    def get_gen(self, index):
        if index < 0 or index >= len(self.genes):
            return None
        return self.genes[index]

    def __str__(self):
        return self.label + ": " + str(self.genes)

class SectionReal(Section):
    def __random_gen(self):
        if self.lsup == None and self.linf == None:
            return norm.rvs()
        elif self.lsup == None:
            return uniform.rvs(self.linf, 2.0*(self.linf+1))
        elif self.linf == None:
            return uniform.rvs(self.lsup - self.lsup, self.lsup)
        return uniform.rvs(self.linf, self.lsup)

    def resize(self, size):
        curr_size = len(self.genes)
        if size > curr_size:
            for i in range(size-curr_size):
                self.genes.append(self.__random_gen())
        elif size < curr_size:
            self.genes = self.genes[:size]

    def random_initialization(self):
        self.genes = []
        for i in range(self.size):
            self.genes.append(self.__random_gen())
        self.sigma = uniform.rvs()

    def mutate(self):
        pass

class SectionInteger(Section):
    def __random_gen(self):
        if self.lsup == None and self.linf == None:
            return randint.rvs(-10,10)
        elif self.lsup == None:
            return randint.rvs(self.linf, 2*(self.linf+1))
        elif self.linf == None:
            return randint.rvs(self.lsup - self.sup, self.lsup)
        return randint.rvs(self.linf, self.lsup)

    def resize(self, size):
        curr_size = len(self.genes)
        if size > curr_size:
            for i in range(size-curr_size):
                self.genes.append(self.__random_gen())
        elif size < curr_size:
            self.genes = self.genes[:size]

    def random_initialization(self):
        self.genes = []
        for i in range(self.size):
            self.genes.append(self.__random_gen())
        self.sigma = uniform.rvs()
            
    def mutate(self):
        pass

class Individual(object):
    def __init__(self):
        self.genoma = []
    def mutate(self):
        for i,v in enumerate(self.genoma):
            v.mutate()

if __name__ == "__main__":
    pass