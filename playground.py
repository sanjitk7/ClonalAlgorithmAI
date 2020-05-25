from deap import creator, base, tools, algorithms
import sys

# register("mutate", tools.mutGaussian, mu=0, sigma=0.5, indpb=0.5)
print(tools.mutGaussian([1,2,3,4],50,10,0.5))

