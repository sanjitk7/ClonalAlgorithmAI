import pandas as pd
import numpy as np
from scipy.spatial import distance

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

def mutateAb(ab,abAttrNames):
    mutatedAb = []
    for attr in ab:
        
    return mutatedAb


n = int(input("Enter 'n' : "))

##t_id,indiscriminate_purchase,purchase_total_compared_customer,expensive_items,card_present,swipe_or_chip,sign_or_pin,freq_recent_purchase,easy_resale_items,geodist_deviation,known_ip,known_mac,time_abnormality,geodist_ship_deviation,known_browser
agPopulation = [[11,20,30,15,1,1,1,60,50,1,1,1,10,1,1],[12,90,60,30,0,0,1,40,80,50,1,0,50,30,0]]

#abPopulation
df_ab = pd.read_csv("/Users/sanjitkumar/personal_projects/clonal-algorithm/credit-card-fraud-detection-with-clonal-algorithm/cardDatasetCsv.csv")

df_ag = pd.DataFrame(agPopulation)

abPoolList = df_ab.values.tolist()
agPoolList = df_ag.values.tolist()

affinityList = []

for i in range(len(df_ag.index)): #for each antigen Ag do
    for j in range(len(df_ab.index)):
        affinityList.append(affinity(list(df_ag.iloc[i]),list(df_ab.iloc[j]),1))
        abPoolSortedList,abPoolSortedDF = makeAbSortPool(affinityList,abPoolList)
    top_n = selectHighest_n(abPoolSortedDF,n)
    clone_set = ()
#     for j in range(n):

# print(sortedAff)
# top_n