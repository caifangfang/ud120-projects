#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
sorted_dict = sorted(data_dict,key=lambda data:data_dict[data]['salary'],reverse=True)
for outlier in sorted_dict:
	if data_dict[outlier]['salary']!='NaN':
		print outlier
		print data_dict[outlier]['salary']
		print data_dict[outlier]['bonus']
		# break
features = ["salary", "bonus"]
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

