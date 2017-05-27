#!/usr/bin/python

# import matplotlib.pyplot as plt
# from prep_terrain_data import makeTerrainData
# from class_vis import prettyPicture,output_image

# features_train, labels_train, features_test, labels_test = makeTerrainData()


# ### the training data (features_train, labels_train) have both "fast" and "slow"
# ### points mixed together--separate them so we can give them different colors
# ### in the scatterplot and identify them visually
# grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
# bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
# grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
# bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


# #### initial visualization
# # plt.xlim(0.0, 1.0)
# # plt.ylim(0.0, 1.0)
# # plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# # plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# # plt.legend()
# # plt.xlabel("bumpiness")
# # plt.ylabel("grade")
# # plt.show()
# ################################################################################


# ### your code here!  name your classifier object clf if you want the 
# ### visualization code (prettyPicture) to show you the decision boundary
# # from sklearn import tree
# # clf = tree.DecisionTreeClassifier(min_samples_split=2)
# from sklearn.neighbors import KNeighborsClassifier
# clf = KNeighborsClassifier(n_neighbors=1)
# # from sklearn.ensemble import AdaBoostClassifier
# # from sklearn.tree import DecisionTreeClassifier
# # clf = AdaBoostClassifier(DecisionTreeClassifier(min_samples_split=40),
# #                          algorithm="SAMME.R",
# #                          n_estimators=200)
# # from sklearn.ensemble import RandomForestClassifier
# # clf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
# clf.fit(features_train,labels_train)
# acc = clf.score(features_test,labels_test)
# # print acc





# try:
#     prettyPicture(clf, features_test, labels_test)
#     output_image("test.png", "png", open("test.png", "rb").read())
#     print acc
# except NameError:
#     print "wrong"


import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
# from sklearn.neighbors import KNeighborsClassifier
# clf = KNeighborsClassifier(n_neighbors=1)
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 
t0 = time()
clf.fit(features_train,labels_train)
print "training time:",round(time()-t0,3),"s"
t1 = time()
pred = clf.predict(features_test)
print "predict time:",round(time()-t1,3),"s"
print clf.score(features_test,labels_test)
from sklearn.metrics import accuracy_score
print accuracy_score(pred,labels_test)
#########################################################