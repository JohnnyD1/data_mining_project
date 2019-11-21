import sys
import csv
import pandas as pd
import numpy as np

def convert(dat_file):

    csv_file = ''.join(dat_file.rsplit('.',1)[0]) + '.csv'

    with open(dat_file, 'r') as dat_f, open(csv_file, 'w') as csv_f:
        csv_writer = csv.writer(csv_f)

        for line in dat_f:
            row = line.split(' ')
            row[-1] = row[-1].strip()
            csv_writer.writerow(row)

    return csv_file     
    
def add_feature_header(csv_file):

    features = ["Age","Sex","Chest_Pain_Type","Resting_Blood_Pressure", \
                "Serum_Cholesterol","Fasting_Blood_Sugar", \
                "Resting_Electrocardiograph_Results", "Maximum_Heart_Rate_Achieved", \
                "Exercise_Induced_Angina", "Oldpeak", \
                "Slope_of_Peak_Exercise_ST_Segment", "#_of_Major_Vessels_Colored_by_Flouroscopy", \
                "Thal", "Presence_of_Heart_Disease"]

    # read csv file with no header feature then write csv file with header features
    old_list = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        # all these values have no decimal portion so they can be converted to ints
        old_list = np.array(list(reader)).astype(float).astype(int)
    df_old = pd.DataFrame(columns=features)
    
    for i in range(len(features)):
        df_old[features[i]] = old_list[:,i]

    df_old.to_csv(csv_file)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = convert(sys.argv[1])
        add_feature_header(filename)
    else:
        print("need to supply argument")
