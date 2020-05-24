from scipy.spatial import distance

def affinity(ag,ab,algo="euclidean"):
    if (algo=="euclidean"):
        return distance.euclidean(ag.get_properties_as_list(),ab.get_properties_as_list())
    elif (algo=="cosine"):
        return distance.cosine(ag.get_properties_as_list(),ab.get_properties_as_list())
    else:
        print("invalid selector")
        return None

