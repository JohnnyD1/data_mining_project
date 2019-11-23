from sklearn.ensemble import RandomForestClassifier

import numpy as np

import sys

def get_training_data(csv_path):
    # read the csv data
    data = np.genfromtxt(csv_path, delimiter=',', skip_header=1)
    # seperate the features and the expected label
    return (data[:,1:-1], data[:,-1])


def data_process(X, y):
    rfc = RandomForestClassifier(n_estimators=100)
    rfc.fit(X[:int(len(X)*0.7)], y[:int(len(y)*0.7)])
    print(rfc.score(X[int(len(X)*0.3):], y[int(len(y)*0.3):]))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        path = "data/heart_proc.csv"
    else:
        path = sys.argv[1]
    X, y = get_training_data(path)
    data_process(X, y, )
