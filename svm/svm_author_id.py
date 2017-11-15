#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
# features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.model_selection import GridSearchCV


def find_best_estimator(features, labels, parameters, estimator=svm.SVC(), n_jobs=100, is_little_data=True):
    gcv = GridSearchCV(estimator, parameters, n_jobs=n_jobs)
    t = time()
    if is_little_data:
        gcv.fit(features[:int(len(features) / 100)], labels[:int(len(labels) / 100)])
    else:
        gcv.fit(features, labels)
    print("find_best_estimator used", round(time() - t, 3), "s    C_best=", gcv.best_estimator_.C, "    score_best=",
          gcv.best_score_)
    return gcv.best_estimator_


if __name__ == "__main__":
    features_train, features_test, labels_train, labels_test = preprocess()
    param = {'kernel': ['rbf'], 'C': range(2400, 2450)}
    clf = svm.SVC(C=find_best_estimator(features_train, labels_train, param).C)
    t = time()
    clf.fit(features_train, labels_train)
    print("fit used", round(time() - t, 3), "s")
    t = time()
    print("score:", clf.score(features_test, labels_test))
    print("predict used", round(time() - t, 3), "s")
    for index in [10, 26, 50]:
        print("predict index=", index, "is", clf.predict([features_test[index]]))


#########################################################
