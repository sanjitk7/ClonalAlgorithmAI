from deap import tools
# from antibody import Antibody

def mutateOneAb(Ab,mut_rate):
    numAttr = Ab.get_all_numeric()
    boolAttr = Ab.get_all_boolean()
    # print(tools.mutGaussian(numAttr,0,mut_rate,0.5))
    Ab.set_all_numeric(tools.mutGaussian(numAttr,0,mut_rate,0.5)[0])
    Ab.set_all_boolean(tools.mutFlipBit(boolAttr,mut_rate)[0])
    return Ab

# print(mutateOneAb(Antibody([1, 10, 1, 2, 0, 0, 0, 1, 5, 30, 1, 0, 1, 10, 1]),1/3).get_properties_as_list())
