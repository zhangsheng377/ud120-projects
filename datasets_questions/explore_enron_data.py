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
import sys

sys.path.append("../final_project/")
from poi_email_addresses import poiEmails

sys.path.append("../tools/")
from feature_format import featureFormat
from feature_format import targetFeatureSplit

if __name__ == "__main__":
    enron_data = pickle.load(
        open("../final_project/final_project_dataset.pkl", "rb"))  # .pkl must use '\r', not the '\r\n'
    # print(enron_data)
    print(len(enron_data))
    print(len(enron_data['METTS MARK']))
    num_POI = 0
    email_list = poiEmails()
    num_email_POI = 0
    num_salary_none = 0
    num_email_none = 0
    num_total_payments_none = 0
    num_POI_total_payments_none = 0
    for name, data in enron_data.items():
        # print(name,data)
        if data['poi']:
            num_POI += 1
            if data['email_address'] in email_list:
                num_email_POI += 1
        if "FASTOW" in name:
            print(name)
        if data['salary'] == "NaN":
            num_salary_none += 1
        if data['email_address'] == "NaN":
            num_email_none += 1
        if data['total_payments'] == "NaN":
            num_total_payments_none += 1
            if data['poi']:
                num_POI_total_payments_none += 1
    print("num_POI:", num_POI)
    print("num_email_POI:", num_email_POI)
    print("enron_data['PRENTICE JAMES']['total_stock_value']:", enron_data['PRENTICE JAMES']['total_stock_value'])
    print("enron_data['COLWELL WESLEY']['from_this_person_to_poi']:",
          enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
    print("enron_data['SKILLING JEFFREY K']['exercised_stock_options']:",
          enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
    print("enron_data['LAY KENNETH L']['total_payments']:", enron_data['LAY KENNETH L']['total_payments'])
    print("enron_data['FASTOW ANDREW S']['total_payments']:", enron_data['FASTOW ANDREW S']['total_payments'])
    print("enron_data['SKILLING JEFFREY K']['total_payments']:", enron_data['SKILLING JEFFREY K']['total_payments'])
    print("num_salary_none:", num_salary_none)
    print("num_email_none:", num_email_none)
    print("num_total_payments_none:", num_total_payments_none, num_total_payments_none * 1.0 / len(enron_data))
    print("num_POI_total_payments_none:", num_POI_total_payments_none,
          num_POI_total_payments_none * 1.0 / len(enron_data))
    feature_list = ["poi", "salary", "bonus"]
    data_array = featureFormat(enron_data, feature_list)
    label, features = targetFeatureSplit(data_array)
    print(label, features)
