# Detect Heart Disease using Random Forests (currently incomplete)

## Preprocessing

We used a dataset consisting of 269 records and 13 features. This dataset can be found [here.](http://archive.ics.uci.edu/ml/datasets/Statlog+%28Heart%29)

The following features already had values as labels:
- 2: Sex: 0,1
- 3: Chest Pain Type: 1,2,3,4
- 6: Fasting Blood Sugar: 0,1
- 7: Resting Electrocardiograph Results: 0,1,2
- 9: Exercise Induced Angina: 0,1
- 10: Oldpeak: 0,1,2,3,4
- 11: Slope of Peak Exercise ST Segment: 1,2,3
- 12: # of Major Vessels Colored by Flouroscopy: 0,1,2,3
- 13: Thal: 3,6,7

The predicted class label is:
- 14: Absence or Presence of Heart Disease: 1,2

We converted the values of the following features into labels:
- 1: Age: 1,2,3,4,5,6
- 4: Resting Blood Pressure: 1,2,3,4,5,6
- 5: Serum Cholesterol: 1,2,3,4,5,6
- 8: Maximum Heart Rate Achieved: 1,2,3,4,5,6

### Method

We used Jenks natural breaks optimization to compute ranges for each of the values.
Jenks natural breaks is essentially kmeans for 1d values. Currently, we use exactly
6 splits for each feature. However, in a future version, we may come up with some
heuristic for choosing the best number of splits for each feature. The original
pre-preprocessed dataset, which can be found in `data/heart.csv`, had all floating
point values. However, there were no decimal portion of the number, so all values
were converted to integers.

### Invocation

`python scripts/preprocess_data.py`


### Output
After running, you can find the output preprocessed data in `data/heart_proc.csv`. You can also find
the split ranges for each feature in `data/centroid_split.txt`.
