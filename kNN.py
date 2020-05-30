import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from copy import deepcopy

def kNN(agVectors):
    cc = pd.read_csv("data/kNNcardDatasetCsv.csv")
    cc1 = cc.drop(['fraud_label','t_id'],axis=1)
    ccTargetLabel = cc["fraud_label"].tolist()
    ccTargetLabelNames = ["not_fraud","fraud"]
    ccDataList = cc1.values.tolist()

    # labelled vectors
    labelledVectors = []

    # Splitting the Dataset (here antibodies) for testing and training
    x_train,x_test,y_train,y_test=train_test_split(ccDataList,ccTargetLabel,random_state=3)

    # initialise kNN classifier and fit the model
    knn=KNeighborsClassifier(n_neighbors=1)
    knn.fit(x_train,y_train)

    # classify a new vector (the to be antigen)
    for vector in agVectors:
        trimVector = deepcopy(vector)
        del(trimVector[0])
        x_new_to_classify=np.array([trimVector])
        prediction_index=knn.predict(x_new_to_classify)
        vector.append(int(prediction_index))
        labelledVectors.append(vector)
        print("Predicted fraud class for vector {} : {}".format(vector,ccTargetLabelNames[int(prediction_index)]))

    print("Test set score (with knn) : {}".format(knn.score(x_test,y_test)))
    return labelledVectors

# classified = kNN([[11,20,30,15,1,1,1,60,50,1,1,1,10,1,1],[12,90,60,30,0,0,1,40,80,50,1,0,50,30,0],[8,12,29,2,0,0,0,43,75,80,1,1,10,40,0]])
# print("classified: ",classified)