'''
This script converts continuous values to labels for a heart disease classification dataset.
You can find this dataset here-> http://archive.ics.uci.edu/ml/datasets/Statlog+%28Heart%29

Need to convert the following features with continuous values into labels:
    1. Age
    4. Resting Blood Pressure
    5. Serum Cholesterol
    8. Maximum Heart Rate Achieved

features that already have values as labels:
    2. Sex: 0,1
    3. Chest Pain Type: 1,2,3,4
    6. Fasting Blood Sugar: 0,1
    7. Resting Electrocardiograph Results: 0,1,2
    9. Exercise Induced Angina: 0,1
    10. Oldpeak: 0,1,2,3,4
    11. Slope of Peak Exercise ST Segment: 1,2,3
    12. # of Major Vessels Colored by Flouroscopy: 0,1,2,3
    13. Thal: 3,6,7
Class Label
    14. Absence or Presence of Heart Disease: 1,2

We will use Jenks natural breaks optimization 
    (which is essentially kmeans for 1d data) 
    to get the ranges for each feature.
For each feature we will use 4 ranges.

TODO: An idea that is not implemented is try
        ranges from 4-7 or so, and find a way to
        determine what gives the best fit
'''

import sys
import jenkspy
import pandas as pd
import csv
import numpy as np

def jenks_algo(cont_feats, centroid_amt=6):
    centroids = []
    # run jenks natural breaks optimization for each feature
    for column in cont_feats:
        centroids.append(jenkspy.jenks_breaks(cont_feats[column].tolist(), centroid_amt))

    # write ranges to file
    with open('../data/centroid_splits.txt', 'w') as f:
        inc = 0
        for column in cont_feats:
            f.write(column + ":\n")
            f.write("\t%s\n" % centroids[inc])
            inc += 1
    
    # update and return df
    inc = 0
    for column in cont_feats:
        ptr1 = 0
        ptr2 = 1
        hack_fix = 0
        while ptr2 < len(centroids[inc]):
            # ptr2 will be the class
            #cont_feats = pd.DataFrame(cont_feats[column].where(~((centroids[inc][ptr1]+hack_fix <= cont_feats[column]) & (cont_feats[column] <= centroids[inc][ptr2])), ptr2),index=cont_feats.index,columns=cont_feats.columns)
            cont_feats[column].where(~((centroids[inc][ptr1]+hack_fix <= cont_feats[column]) & (cont_feats[column] <= centroids[inc][ptr2])), ptr2, inplace=True)
            hack_fix = 1
            ptr1 += 1
            ptr2 += 1
        inc += 1

    return cont_feats
    

def run(csv_file):

    df_final = pd.read_csv(csv_file)

    # extract features that need values to be assigned to ranges
    cont_features_idx = [1,4,5,8]
    label_features = jenks_algo(df_final.iloc[:,cont_features_idx].copy())
    #print(label_features)
    # combine new features with df
    for features in label_features:
        df_final[features] = label_features[features]

    # write to csv
    name = csv_file.rsplit('.',1)[0]
    df_final.to_csv(name + "_proc.csv",index=False)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        print("need to supply csv file")
