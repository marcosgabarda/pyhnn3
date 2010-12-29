import sys
import mlpy
import numpy

__author__="Marcos Gabarda"
__date__ ="$06-dic-2010 16:19:56$"

class OutputNeuron:
    
    def __init__(self, mode):
        self.__mode = mode
        self.__weights = []
    
    def __function_sigmoid(self, value):
        return 1 / (1 + numpy.exp(-value))

    def __function_logit(self, value):
        return numpy.ln(value/(1-value))

    def __activation_function(self, value):
        if self.__mode == "reg":
            return value
        return self.__function_sigmoid(value)

    def __ridge_regression(self, X, t, l):
        hn = len(X[0])
        rr = mlpy.RidgeRegression(alpha=l)
        x = numpy.array(X)
        y = numpy.array(t)
        rr.learn(x, y)
        beta = rr.beta()
        self.__weights = []
        for i in range(hn):
            self.__weights.append(beta[i])

    def __ridge_regression_classification_fix(self, X, t, l):
        hn = len(X[0])
        rr = mlpy.RidgeRegression(alpha=l)
        x = numpy.array(X)
        y = numpy.array(t)
        for i in range(len(y)):
            if y[i] == 0:
                y[i] = self.__function_logit(0.1)
            elif y[i] == 1:
                y[i] = self.__function_logit(0.9)
        rr.learn(x, y)
        beta = rr.beta()
        self.__weights = []
        for i in range(hn):
            self.__weights.append(beta[i])

    def train(self, X, t, l):
        if self.__mode == "reg":
            self.__ridge_regression(X, t, l)
        else:
            self.__ridge_regression_classification_fix(X, t, l)

    def set_weights(self, weights):
        self.__weights = weights

    def get_output(self, values):
        # @type values: list

        # Check weights size and values size
        if len(self.__weights) != len(values) + 1:
            sys.stderr.write('Error - Training of output layer needed.\n')
            exit(-1)

        sum = 0.0
        for i in range(len(values)):
            sum += self.__weights[i] * values[i]
        sum += self.__weights[len(self.__weights) - 1]
        return self.__activation_function(sum)

if __name__ == "__main__":
    pass