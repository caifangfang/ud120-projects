#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# print len(enron_data["SKILLING JEFFREY K"])
# poi_count = 0
'''
{'salary': 274975, 'to_messages': 873, 'deferral_payments': 'NaN', 'total_paymen
ts': 1272284, 'exercised_stock_options': 384728, 'bonus': 600000, 'restricted_st
ock': 393818, 'shared_receipt_with_poi': 874, 'restricted_stock_deferred': 'NaN'
, 'total_stock_value': 778546, 'expenses': 125978, 'loan_advances': 'NaN', 'from
_messages': 16, 'other': 200308, 'from_this_person_to_poi': 6, 'poi': True, 'dir
ector_fees': 'NaN', 'deferred_income': 'NaN', 'long_term_incentive': 71023, 'ema
il_address': 'ben.glisan@enron.com', 'from_poi_to_this_person': 52}
'''
# print enron_data["COLWELL WESLEY"]
# count_salary = 0
# count_mailbox = 0
count_nan_payments = 10
count_poi = 10
# print len(enron_data)
for person in enron_data:
	# print person
	# if enron_data[person]['salary'] != 'NaN':
	# 	count_salary += 1
	# if enron_data[person]['email_address'] != 'NaN':
	# 	count_mailbox += 1
	if enron_data[person]['poi']==True:
		count_poi += 1
		if enron_data[person]['total_payments'] == 'NaN':
			count_nan_payments += 1

print count_poi
print count_nan_payments
print count_nan_payments*1.0/count_poi
# print count_salary
# print count_mailbox
	# if person.find("PRENTICE JAMES")>=0:
	# 	print enron_data[person]['total_stock_value']
	# 	break
# 	if enron_data[person]["poi"]==True:
# 		poi_count += 1
	
# print poi_count

# print enron_data["Skilling Jeffrey K".upper()]['total_payments']
# print enron_data["Lay Kenneth L".upper()]['total_payments']
# print enron_data["Fastow Andrew S".upper()]['total_payments']

