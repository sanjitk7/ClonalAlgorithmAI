import pandas as pd
import numpy as np
from copy import deepcopy
from antibody import Antibody
from affinity import affinity
from mutation import mutateOneAb
import configparser
import operator
from kNN import kNN

def makeAbSortedDF(abPoolList):
    abSortedPool = pd.DataFrame(abPoolList)
    abSortedPool.columns = df_ab.columns
    return abSortedPool

def makeAbSortPool(affinityList, abPopulation):
    yx = list(zip(affinityList, abPopulation))
    print("\nyx before sort:",yx)
    sortedAb = sorted(yx, key=operator.itemgetter(0))
    print("\nyx after sort:",sortedAb)
    abPool_sorted = [x for y, x in sortedAb]
    return abPool_sorted

def selectHighest_n(abPoolSortedDF,n):
#     abPoolSortedDF_n = abPoolSortedDF.index < n
#     abPoolSortedDF_n = abPoolSortedDF.index()
    abPoolSortedDF_n = abPoolSortedDF[(abPoolSortedDF.index < n)]
    return abPoolSortedDF_n

# Creates antibodies or antigen population
def instantiate_population(PoolList):
    # list of antibodies as objects
    populationList = []
    for vector in PoolList:
        # Class Antibody creates Ab or Ag (similar structure)
        populationList.append(Antibody(vector))
    return populationList

if (__name__=="__main__"):
    # n = int(input("Enter 'n' : "))
    # beta = float(input("Enter beta : "))
    cfg = configparser.ConfigParser()
    cfg.read("config.ini")
    beta=cfg.getfloat("general","beta") # Clone Factor
    d = cfg.getint("general","d")
    G = cfg.getint("general","G")# Number of generations

    #abPopulation
    df_ab = pd.read_csv("data/kNNcardDatasetCsv.csv")
    # df_ag = pd.DataFrame(agPopulation)
    abPoolList = df_ab.values.tolist()
    abPopulation = instantiate_population(abPoolList)

    n = len(abPopulation)//3


    df_ag = pd.read_csv("data/attackVector.csv")
    agPoolList = df_ag.values.tolist()
    agPopulation = instantiate_population(agPoolList)

    ##t_id,indiscriminate_purchase,purchase_total_compared_customer,expensive_items,card_present,swipe_or_chip,sign_or_pin,freq_recent_purchase,easy_resale_items,geodist_deviation,known_ip,known_mac,time_abnormality,geodist_ship_deviation,known_browser
    # agPopulation = [[11,20,30,15,1,1,1,60,50,1,1,1,10,1,1],[12,90,60,30,0,0,1,40,80,50,1,0,50,30,0]]

    N = len(abPoolList)
    for generation in range(G):
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        print("Generation #",generation+1)
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        print("\nAg Population Size:\n",len(agPopulation))
        for i in range(len(agPopulation)): #for each antigen Ag do
            affinityList = []
            print("-----------------------------------------------------------------------")
            print("Current Ag : ",agPopulation[i].toString())
            print("-----------------------------------------------------------------------")
            for j in range(1,len(df_ab.index)):
                # print("ag lis:",agPopulation[i].get_properties_as_list())
                # print("ab lis:",abPopulation[j].get_properties_as_list())
                affinityList.append(affinity(agPopulation[i],abPopulation[j],"cosine"))
                # keep in mind that the affinity here is literally the distance. So More the distance, lesser the affinity
                # might have to consider doing (1 - distance) for affinity later
            print("\nAffinity List: ",affinityList)
            abPoolSortedList = makeAbSortPool(affinityList,abPopulation)
            print("\nSorted AntiBodies: ",abPoolSortedList)

            # print(abPoolSortedDF)
            # Selecting n highest affinity Ab
            top_n = abPoolSortedList[:n]
            # print(top_n)
            # clone_set = ()
            cloneSet = []
            currentClonesList = []
            for k in range(0,n):
                currentAb = top_n[k]
                # --------------------------Cloning Step----------------------------- #
                x = (beta*N)//(k+1)
                for l in range(int(x)):
                    currentClonesList.append(deepcopy(currentAb))
                print("\nCurrent clones after cloning: \n",currentClonesList)
                # --------------------------Mutation Step----------------------------- #
                for currentClone in currentClonesList:
                    cloneSet.append(mutateOneAb(currentClone,(k+1)/n))
                    # mutation doest alter tid so we might get duplicates
                print("\nMutated Clones (current clone set): \n",cloneSet)
                #------------------Clone Set Compare and Union with Memory Pool--------#
                #------------------Get Ab p with highest affinity p’ from C S----------#
                highestCloneAff = 1
                for clone in cloneSet:
                    currentCloneAff = affinity(agPopulation[i],clone,"cosine")
                    if (highestCloneAff > currentCloneAff):
                        highestCloneAff = currentCloneAff
                        highestAffClone = clone
                print("\nHighest Affinity Clone (Affinity - ",highestCloneAff,") in current clone set: \n",highestAffClone.toString())
                #------------------Get Ab q with highest affinity q’ from---------------#
                highestMemAbAff = 1
                for ab in abPopulation:
                    currentMemAbAff = affinity(agPopulation[i],ab,"cosine")
                    if (highestMemAbAff > currentMemAbAff):
                        highestMemAbAff = currentMemAbAff
                        # highestAffMemAbIndex = 
                        highestAffMemAb = ab
                print("\nHighest Affinity Antibody (Affinity - ",highestMemAbAff,") from Memorty Pool: \n",highestAffMemAb.toString())
                #------------------If p’ is greater than q’ replace q per p------------#
                if (highestCloneAff > highestMemAbAff):
                    abPopulation.remove(highestAffMemAb)
                    abPopulation.append(highestAffClone)
                    print("\n****REPLACEMENT*****\n")
                    print("Replaced Antibody from Memory Pool:\n",highestAffMemAb.toString())
                    print("\nReplaced with clone:\n",highestAffClone.toString())
                else:
                    print("\n****NO REPLACEMENT*****\n")
            
            #------------------Replace the d lowest affinity by new generated Abs-------#

            # Check if aff(highestAffAb) > threshold aff -> Check no label -> kNN label -> label ag -> next ag
            # if (highestMemAbAff < thresholdAff):
                #if (highestMemAb has no label):
                
            # ????? for now we lets assume to replace 0 antibodies
            # for kk in range(n,N):
                # replace ab in mempool with new random antibody

            



    # print(sortedAff)
    # top_n