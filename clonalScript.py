import pandas as pd
import numpy as np
from scipy.spatial import distance
from copy import copy

def affinity(ag,ab,algo):
    if (algo==0):
        return distance.euclidean(ag,ab)
    elif (algo==1):
        return distance.cosine(ag,ab)
    else:
        print("invalid selector")
        return None

def makeAbSortedDF(abPoolList):
    abSortedPool = pd.DataFrame(abPoolList)
    abSortedPool.columns = df_ab.columns
    return abSortedPool

def makeAbSortPool(affinityList, abPoolList):
    yx = list(zip(affinityList, abPoolList))
    yx.sort()
    abPool_sorted = [x for y, x in yx]
    return abPool_sorted, makeAbSortedDF(abPool_sorted)

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


# incorporate some attribute wise explicit data manipulation feature later



# n = int(input("Enter 'n' : "))
# beta = float(input("Enter beta : "))
n=3
beta=0.5
d = 5

##t_id,indiscriminate_purchase,purchase_total_compared_customer,expensive_items,card_present,swipe_or_chip,sign_or_pin,freq_recent_purchase,easy_resale_items,geodist_deviation,known_ip,known_mac,time_abnormality,geodist_ship_deviation,known_browser
agPopulation = [[11,20,30,15,1,1,1,60,50,1,1,1,10,1,1],[12,90,60,30,0,0,1,40,80,50,1,0,50,30,0]]

#abPopulation
df_ab = pd.read_csv("cardDatasetCsv.csv")

df_ag = pd.DataFrame(agPopulation)

abPoolList = df_ab.values.tolist()
agPoolList = df_ag.values.tolist()

N = len(abPoolList)

for i in range(len(df_ag.index)): #for each antigen Ag do
    affinityList = []
    print("-----------------------------------------------------------------------")
    print("Current Ag : ",list(df_ag.iloc[i]))
    print("-----------------------------------------------------------------------")
    for j in range(len(df_ab.index)):
        affinityList.append(affinity(list(df_ag.iloc[i]),list(df_ab.iloc[j]),1))
    abPoolSortedList,abPoolSortedDF = makeAbSortPool(affinityList,abPoolList)
    # print(abPoolSortedDF)
    top_n = selectHighest_n(abPoolSortedDF,n).values.tolist()
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
            mutatedClonesList.append(mutateOne(currentClone,[],(k+1)/n,n))
        currentClonesSet = set(tuple(i) for i in currentClonesList)
        mutatedClonesSet = set(tuple(i) for i in mutatedClonesList)
        currentClonesSet.union(mutatedClonesSet)
        print("Cloned and Unioned with Mutated Ab: ",currentClonesSet)
        affinityGreatest = 0
        # Get Ab p with highest affinity p’ from C S
        for y in currentClonesSet:
            if (affinity(list(df_ag.iloc[i]),y,1) > affinityGreatest):
                affinityGreatestAbCS = y
        # Get Ab q with highest affinity q’ from
        # If p’ is greater than q’ replace q per p;
        if (affinityGreatestAbCS > abPoolSortedList[0]):
            abPoolSortedList[0]=affinityGreatestAbCS
    # Replace the d lowest affinity by new generated Abs
        
        #ID???
        # print("Clone Set for n=",k+1," : ",currentClones)
        # print("Mutated Set for n=",k+1," : ",mutatedClones)
        

        # print("mutation rate: ",float(k+1/n))

        



# print(sortedAff)
# top_n