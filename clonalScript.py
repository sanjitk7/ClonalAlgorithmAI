import pandas as pd
import numpy as np
from copy import deepcopy
from antibody import Antibody
from affinity import affinity
from mutation import mutateOneAb

def makeAbSortedDF(abPoolList):
    abSortedPool = pd.DataFrame(abPoolList)
    abSortedPool.columns = df_ab.columns
    return abSortedPool

def makeAbSortPool(affinityList, abPopulation):
    yx = list(zip(affinityList, abPopulation))
    yx.sort()
    abPool_sorted = [x for y, x in yx]
    return abPool_sorted

def selectHighest_n(abPoolSortedDF,n):
#     abPoolSortedDF_n = abPoolSortedDF.index < n
#     abPoolSortedDF_n = abPoolSortedDF.index()
    abPoolSortedDF_n = abPoolSortedDF[(abPoolSortedDF.index < n)]
    return abPoolSortedDF_n

#ip: clone list of current Ab
#op: list of mutated Ab with current mutation rate
def mutateOne(ab,abAttrNames,mr,n):
    abList = ab.get_properties_as_list()
    mutatedAb = []
    scaled_mr = 7*(mr - 0)/n-0 #scaled to 0-7 to flip bits appropriately because range of the int colums is always 0-100 an len(bin(100))=7
    for attrVal in abList:
        if(type(attrVal)==int):
            binAttrVal = f'{attrVal:07b}'
            newBinAttrVal = list(binAttrVal)
            if (newBinAttrVal[int(scaled_mr)]==0):
                newBinAttrVal[int(scaled_mr)] =1
            else:
                newBinAttrVal[int(scaled_mr)]=0
            newBinAttrVal = "".join(str(digit) for digit in newBinAttrVal)
            mutatedAttr = int(newBinAttrVal,2)
            mutatedAb.append(mutatedAttr)
        elif(type(attrVal)==bool):
            if (scaled_mr > 3.5):
                if (attrVal == True):
                    mutatedAttr = 0
                else:
                    mutatedAttr = 1
                mutatedAb.append(mutatedAttr)
            # else:
                # print("No Change req as not enough mr")
        else:
            print("TypeError in Ab Attr", attrVal)

    return Antibody(mutatedAb)

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
    beta=0.5 # Clone Factor
    d = 5
    G = 20 # Number of generations

    #abPopulation
    df_ab = pd.read_csv("cardDatasetCsv.csv")
    # df_ag = pd.DataFrame(agPopulation)
    abPoolList = df_ab.values.tolist()
    abPopulation = instantiate_population(abPoolList)

    n = len(abPopulation)//3

    df_ag = pd.read_csv("attackVector.csv")
    agPoolList = df_ag.values.tolist()
    agPopulation = instantiate_population(agPoolList)

    ##t_id,indiscriminate_purchase,purchase_total_compared_customer,expensive_items,card_present,swipe_or_chip,sign_or_pin,freq_recent_purchase,easy_resale_items,geodist_deviation,known_ip,known_mac,time_abnormality,geodist_ship_deviation,known_browser
    # agPopulation = [[11,20,30,15,1,1,1,60,50,1,1,1,10,1,1],[12,90,60,30,0,0,1,40,80,50,1,0,50,30,0]]

    N = len(abPoolList)
    for generation in range(G):
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        print("Generation #",generation+1)
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        print("Ag Population Size:",len(agPopulation))
        for i in range(len(agPopulation)): #for each antigen Ag do
            affinityList = []
            print("-----------------------------------------------------------------------")
            print("Current Ag : ",agPopulation[i].toString())
            print("-----------------------------------------------------------------------")
            for j in range(1,len(df_ab.index)):
                # print("ag lis:",agPopulation[i].get_properties_as_list())
                # print("ab lis:",abPopulation[j].get_properties_as_list())
                affinityList.append(affinity(agPopulation[i],abPopulation[j],"cosine"))
            print("Affinity List: ",affinityList)
            abPoolSortedList = makeAbSortPool(affinityList,abPopulation)
            print("Sorted AntiBodies: ",abPoolSortedList)

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
                print("Current clones after cloning: ",currentClonesList)
                # --------------------------Mutation Step----------------------------- #
                for currentClone in currentClonesList:
                    cloneSet.append(mutateOneAb(currentClone,(k+1)/n))
                print("Mutated Clones (current clone set): ",cloneSet)
                #------------------Clone Set Compare and Union with Memory Pool--------#
                #------------------Get Ab p with highest affinity p’ from C S----------#
                highestCloneAff = 0
                for clone in cloneSet:
                    currentCloneAff = affinity(agPopulation[i],clone,"cosine")
                    if (highestCloneAff < currentCloneAff):
                        highestAffClone = clone
                print("Highest Affinity Clone in current clone set: ",highestAffClone.get_properties_as_list())
                #------------------Get Ab q with highest affinity q’ from---------------#
                #------------------If p’ is greater than q’ replace q per p------------#
                
            # Replace the d lowest affinity by new generated Abs
            # for kk in range(n,N):
                # replace ab in mempool with new random antibody
            
                # print("Clone Set for n=",k+1," : ",currentClones)
                # print("Mutated Set for n=",k+1," : ",mutatedClones)
                

                # print("mutation rate: ",float(k+1/n))

            



    # print(sortedAff)
    # top_n