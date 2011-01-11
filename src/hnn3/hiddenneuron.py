import numpy

__author__="Marcos Gabarda"
__date__ ="$06-dic-2010 16:19:37$"

class HiddenNeuron:
    """
    Hidden Neuron
    """
    def __init__(self, center, gamma, q):
        # @type self.center: Input
        # @type gamma: float
        # @type q: float
        self.center = center
        self.gamma = gamma
        self.q = q
        
    def __activation_function(self, value):
        return 1 / (1 + numpy.exp(-value))

    def get_output(self, input):
        # @type input: Input
        sim = self.center.similarity(input, self.q)
        return self.__activation_function(sim*self.gamma)


if __name__ == "__main__":
    pass
