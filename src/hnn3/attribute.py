import numpy
import math

__author__="Marcos Gabarda"
__date__ ="$06-dic-2010 17:09:21$"

class Attribute:
    """
    Abstract attribute from the input set.
    """
    data_set = None
    missing = False
    value = None
    
    def s_r(self, z, alpha, beta):
        return numpy.power((1 - numpy.power(z, beta)), alpha)
        
    def s_n(self, z):
        return 1 / (1 + z)

    def similarity(self, attr):
        pass
    
    def __str__(self):
        if self.missing:
            return "Missing"
        return str(self.value)

class IntegerAttribute(Attribute):
    def similarity(self, attr):
        if attr.missing or self.missing:
            return 0.0
        return self.s_n(math.fabs( attr.value - self.value))

class RealAttribute(Attribute):
    def similarity(self, attr):
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
        # TODO
        pass
    
class NominalAttribute(Attribute):
    headers = []
    def similarity(self, attr):
        if attr.value == self.value:
            return 1.0
        return 0.0
    
class BinaryAttribute(Attribute):
    headers = [0, 1]
    def similarity(self, attr):
        # TODO
        pass
    
class FuzzyAttribute(Attribute):
    def similarity(self, attr):
        # TODO
        pass
    
if __name__ == "__main__":
    x = IntegerAttribute()
    x.value = 10
    y = IntegerAttribute()
    y.value = 10
    print y.similarity(x)
    x = RealAttribute()
    x.value = 10.1
    y = RealAttribute()
    y.value = 10.1
    print y.similarity(x)

