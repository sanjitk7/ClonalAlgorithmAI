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

mutatedAb = mutateOne([1,2,3,4,5],[],2.3,3)
print(mutatedAb)

# incorporate some attribute wise explicit data manipulation feature later
