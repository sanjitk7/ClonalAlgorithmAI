import pandas as pd
import numpy as np
from copy import copy
from antibody import Antibody
from affinity import affinity

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
    mutatedAb = []
    scaled_mr = 7*(mr - 0)/n-0 #scaled to 0-7 to flip bits appropriately because range of the int colums is always 0-100 an len(bin(100))=7
    for attrVal in ab:
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
                if (attrVal == 1):
                    mutatedAttr = 0
                else:
                    mutatedAttr = 1
                mutatedAb.append(mutatedAttr)
            # else:
                # print("No Change req as not enough mr")
        else:
            print("TypeError in Ab Attr", attrVal)
    return mutatedAb

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
            top_n = abPoolSortedList[:n]

            # -------------------------- Stopped Here
            # print(top_n)
            # clone_set = ()
            currentClonesList = []
            mutatedClonesList = []
            for k in range(0,n):
                currentAb = top_n[k]
                x = (beta*N)//(k+1)
                for l in range(int(x)):
                    currentClonesList.append(copy(currentAb))
                for currentClone in currentClonesList:
                    #ID??? is also mutated?????
                    mutatedClonesList.append(mutateOne(currentClone,[],(k+1)/n,n))
                currentClonesSet = set(tuple(i) for i in currentClonesList)
                mutatedClonesSet = set(tuple(i) for i in mutatedClonesList)
                currentClonesSet.union(mutatedClonesSet)
                print("Cloned and Unioned with Mutated Ab: ",currentClonesSet)
                affinityGreatest = 0
                # Get Ab p with highest affinity p’ from C S
                for y in currentClonesSet:
                    if (affinity(list(df_ag.iloc[i]),y,"cosine") > affinityGreatest):
                        affinityGreatestAbCS = y
                # Get Ab q with highest affinity q’ from
                # If p’ is greater than q’ replace q per p;
                if (affinityGreatest > affinityList[0]):
                    abPoolSortedList[0]=affinityGreatestAbCS
            # Replace the d lowest affinity by new generated Abs
            # for kk in range(n,N):
                # replace ab in mempool with new random antibody
            
                # print("Clone Set for n=",k+1," : ",currentClones)
                # print("Mutated Set for n=",k+1," : ",mutatedClones)
                

                # print("mutation rate: ",float(k+1/n))

            



    # print(sortedAff)
    # top_n