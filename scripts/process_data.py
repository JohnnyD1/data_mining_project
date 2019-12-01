from sklearn.ensemble import RandomForestClassifier

import numpy as np

import sys
import os

def get_training_data(csv_path):
    # read the csv data
    data = np.genfromtxt(csv_path, delimiter=',', skip_header=1)
    # seperate the features and the expected label
    return (data[:,:-1], data[:,-1])

def get_label_data(csv_path):
    data = np.genfromtxt(csv_path, delimiter=',', skip_header=1)
    return data

def train_rfc(X, y):
    rfc = RandomForestClassifier(n_estimators=100)
    rfc.fit(X, y)
    return rfc

def write_predicted(csv_path, data, labels):
    full_data = np.append(data, np.expand_dims(labels,1), axis=1)
    np.savetxt(csv_path, full_data, delimiter=',')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        train = sys.argv[1]
        X, y = get_training_data(train)
        rfc = train_rfc(X[:int(len(X)*0.7)], y[:int(len(y)*0.7)])
        print("Accuracy: ", rfc.score(X[int(len(X)*0.7):], y[int(len(y)*0.7):]))        
    elif len(sys.argv) == 3:
        train = sys.argv[1]
        X, y = get_training_data(train)
        rfc = train_rfc(X, y)
        label = sys.argv[2]
        Z = get_label_data(label)
        predicted = rfc.predict(Z)
        write_predicted(os.path.splitext(label)[0] + '_predicted.csv', Z, predicted)
    else:
        print("Pass csv files as args")
