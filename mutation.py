from deap import tools
# from antibody import Antibody

def mutateOneAb(Ab,mut_rate):
    numAttr = Ab.get_all_numeric()
    boolAttr = Ab.get_all_boolean()
    # print(tools.mutGaussian(numAttr,0,mut_rate,0.5))
    Ab.set_all_numeric(tools.mutGaussian(numAttr,0,mut_rate,1)[0])
    Ab.set_all_boolean(tools.mutFlipBit(boolAttr,mut_rate)[0])
    return Ab
