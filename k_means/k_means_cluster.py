#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()

def featureScaling(arr):
    new_data = []
    sort_arr = arr
    sort_arr.sort()
    min_arr = sort_arr[0]
    max_arr = sort_arr[-1]
    if min_arr==max_arr:
        return [0.5]*len(arr)
    else:
        for i in arr:
            new_data.append((i-min_arr)*1.0/(max_arr-min_arr))
        return new_data

### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

### return min and max value of exercised_stock_options
min_stock = 0
max_stock = 0
for data in data_dict:
	curr_stock = data_dict[data]['exercised_stock_options']
	if curr_stock!='NaN':
		if min_stock==0:
			min_stock = curr_stock
		elif min_stock>curr_stock:
			min_stock = curr_stock
		if max_stock ==0:
			max_stock = curr_stock
		elif max_stock<curr_stock:
			max_stock = curr_stock
print min_stock
print max_stock
print (1000000-min_stock)*1.0/(max_stock-min_stock)

### return min and max value of salary
min_salary = 0
max_salary = 0
for data in data_dict:
	curr_salary = data_dict[data]['salary']
	if curr_salary!='NaN':
		if min_salary==0:
			min_salary = curr_salary
		elif min_salary>curr_salary:
			min_salary = curr_salary
		if max_salary ==0:
			max_salary = curr_salary
		elif max_salary<curr_salary:
			max_salary = curr_salary
print min_salary
print max_salary
print (200000-min_salary)*1.0/(max_salary-min_salary)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
# feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler()
finance_features_scalered = min_max_scaler.fit_transform(finance_features)
from sklearn.cluster import KMeans
pred = KMeans(n_clusters=2).fit_predict(finance_features_scalered)



### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
