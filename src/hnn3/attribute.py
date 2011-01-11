import numpy
import math

__author__="Marcos Gabarda"
__date__ ="$06-dic-2010 17:09:21$"

class Attribute:
    """

    Abstract attribute from the input set.

    @type data_set: InputSet
    """
    data_set = None
    missing = False
    value = None
    index = None
    
    def s_r(self, z, alpha, beta):
        return numpy.power((1 - numpy.power(z, beta)), alpha)
        
    def s_n(self, z):
        return 1 / (1 + z)

    def similarity(self, attr):
        # @type attr: Attribute
        pass
    
    def __str__(self):
        if self.missing:
            return "Missing"
        return str(self.value)

class IntegerAttribute(Attribute):
    def similarity(self, attr):
        # @type attr: Attribute
        if attr.missing or self.missing:
            return 0.0
        return self.s_n(math.fabs( attr.value - self.value))

class RealAttribute(Attribute):
    def similarity(self, attr):
        """
        @type attr: Attribute
        """
        if attr.missing or self.missing:
            return 0.0
        num = math.fabs( attr.value - self.value)
        den = self.data_set.sup
        if not den:
            if attr.value > self.value:
                den = attr.value
            else:
                den = self.value
        return self.s_r(num / den, 2, 1)
    
class OrdinalAttribute(Attribute):
    headers = []
    def similarity(self, attr):
        # @type Attribute
        if attr.missing or self.missing:
            return 0.0
        index_i = self.headers.index(attr.value)
        index_j = self.headers.index(self.value)
        if index_j < index_i:
            tmp = index_i
            index_i = index_j
            index_j = tmp
        l = self.headers[index_i:index_j+1]
        num = 0.0
        for i in range(len(l)):
            num += self.data_set.get_attribute_probability(self.index, l[i])
        num = 2 * numpy.log(num)
        if num == 0.0:
            return 0.0
        den = numpy.log(self.data_set.get_attribute_probability(self.index, self.value)) \
            + numpy.log(self.data_set.get_attribute_probability(self.index, attr.value))
        return num/den
    
class NominalAttribute(Attribute):
    headers = []
    def similarity(self, attr):
        # @type Attribute
        if attr.missing or self.missing:
            return 0.0
        if attr.value == self.value:
            return 1.0
        return 0.0
    
class BinaryAttribute(Attribute):
    headers = [0, 1]
    def similarity(self, attr):
        # @type Attribute
        if attr.missing or self.missing:
            return 0.0
        if attr.value == self.value:
            p = self.data_set.get_attribute_probability(self.index, self.value)
            return (2 * numpy.log(p+p))/(numpy.log(p)+numpy.log(p))
        else:
            p0 = self.data_set.get_attribute_probability(self.index, 0)
            p1 = self.data_set.get_attribute_probability(self.index, 1)
            return (2 * numpy.log(p0+p1))/(numpy.log(p0)+numpy.log(p1))
    
class FuzzyAttribute(Attribute):
    def similarity(self, attr):
        # @type Attribute
        # TODO
        pass
    
if __name__ == "__main__":
    pass

