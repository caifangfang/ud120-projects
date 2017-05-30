#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

### it's all yours from here forward!  
clf = DTC()
clf.fit(features_train,labels_train)
# print "first accuracy(overfitting):",clf.score(features,labels)
print "accuracy on train data:",clf.score(features_train,labels_train)
print "accuracy on test data:",clf.score(features_test,labels_test)
pred = clf.predict(features_test)
print "predict result:",pred
print "test data no.:",len(labels_test)
print "precision_score:",precision_score(pred,labels_test)
print "recall_score:",recall_score(pred,labels_test)