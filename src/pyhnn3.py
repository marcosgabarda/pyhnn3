import argparse
from ees.environment import EESEnvironment
from hnn3.individual import IndividualHNN3
from hnn3.inputset import InputSet

__author__="Marcos Gabarda"
__date__ ="$04-dic-2010 17:34:16$"

if __name__ == "__main__":
    # @type data_set: InputSet
    # @type ess: EESEnvironment
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset', help='problem data set')
    parser.add_argument('-n', type=int, help='initial population', required=True)
    #parser.add_argument('-t', type=int, help='maximitation or minimzation problem')
    #parser.add_argument('-r', type=int, help='replacement mode')
    args = parser.parse_args()

    data_set = InputSet()
    data_set.load(args.dataset)
    ees = EESEnvironment(data_set, IndividualHNN3, args.n)
    ees.run()
