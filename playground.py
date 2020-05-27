# from deap import creator, base, tools, algorithms
# import sys
from antibody import Antibody
import operator

# # register("mutate", tools.mutGaussian, mu=0, sigma=0.5, indpb=0.5)
# print(tools.mutGaussian([1,2,3,4],50,10,0.5))

yx = [(0.5,Antibody([1, 10, 1, 2, 0, 0, 0, 1, 5, 30, 1, 0, 1, 10, 1])),
(0.1,Antibody([1, 10, 1, 2, 0, 0, 0, 1, 5, 30, 1, 0, 1, 20, 1])),
(0.1,Antibody([1, 10, 1, 2, 0, 0, 0, 1, 5, 30, 1, 0, 1, 20, 1]))]
# print(yx.sort())
sortedList = sorted(yx, key=operator.itemgetter(0))
print("yay list sorted: ",sortedList)