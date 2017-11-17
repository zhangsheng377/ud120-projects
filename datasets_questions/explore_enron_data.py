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

if __name__ == "__main__":
    enron_data = pickle.load(
        open("../final_project/final_project_dataset.pkl", "rb"))  # .pkl must use '\r', not the '\r\n'
    # print(enron_data)
    print(len(enron_data))
    print(len(enron_data['METTS MARK']))
    num_POI = 0
    email_list = poiEmails()
    num_email = 0
    for name, data in enron_data.items():
        # print(name,data)
        if data['poi']:
            num_POI += 1
            if data['email_address'] in email_list:
                num_email += 1
    print("num_POI:", num_POI)
    print("num_email:", num_email)
