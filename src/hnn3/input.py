import numpy

__author__="Marcos Gabarda"
__date__ ="$06-dic-2010 17:09:13$"

class Input:
    attributes = []
    target = []

    def __init__(self, attributes):
        # @type attributes: list
        self.attributes = attributes
        self.target = []

    def __q_mean(self, partial, q):
        # @type partial: list
        # @type q: float
        if q != 0:
            sum = 0.0
            for i in range(len(partial)):
                if partial[i] != 0:
                    sum += numpy.power(partial[i], q)
            res = sum / float(len(partial))
            return numpy.power(res, (1.0/q))
        else:
            pow = 0.0
            for i in range(len(partial)):
                pow *= partial[i]
            return numpy.power(pow, float(len(partial)))

    def similarity(self, input, q):
        # @type input: Input
        s = []
        size = len(input.attributes)
        if len(self.attributes) < size:
            size = len(self.attributes)
        for i in range(size):
            ax = self.attributes[i]
            ay = input.attributes[i]
            s.append(ax.similarity(ay))
        return self.__q_mean(s, q)

    def __str__(self):
        return "Attrs: " + str(map(str, self.attributes)) + " Target: " \
               + str(self.target)

if __name__ == "__main__":
    input = Input([1, "a"])
