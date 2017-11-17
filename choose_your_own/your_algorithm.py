#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from matplotlib import image as mpimg
from time import time


def find_best_estimator(features, labels, parameters, estimator, n_jobs=100, is_little_data=True):
    gcv = GridSearchCV(estimator, parameters, n_jobs=n_jobs)
    t = time()
    if is_little_data:
        gcv.fit(features[:int(len(features) / 100)], labels[:int(len(labels) / 100)])
    else:
        gcv.fit(features, labels)
    print("find_best_estimator used", round(time() - t, 3), "s    score_best=", gcv.best_score_, "    best_estimator:",
          gcv.best_estimator_)
    return gcv


def show_image(classifier, features, labels):
    try:
        prettyPicture(classifier, features, labels)
    except NameError:
        pass

    plt.imshow(mpimg.imread("test.png"))
    plt.show()


if __name__ == '__main__':
    features_train, labels_train, features_test, labels_test = makeTerrainData()

    ### the training data (features_train, labels_train) have both "fast" and "slow"
    ### points mixed together--separate them so we can give them different colors
    ### in the scatterplot and identify them visually
    grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
    bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
    grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
    bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]

    #### initial visualization
    '''plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
    plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")
    plt.show()'''
    ################################################################################


    ### your code here!  name your classifier object clf if you want the
    ### visualization code (prettyPicture) to show you the decision boundary
    clf = GaussianNB()
    t = time()
    clf.fit(features_train, labels_train)
    print("fit used", round(time() - t, 3), "s")
    print("GaussianNB:", clf.score(features_test, labels_test))
    # show_image(clf, features_test, labels_test)

    parameters = {'kernel': ['linear'], 'C': range(30, 10000)}
    t = time()
    # clf = find_best_estimator(features_train, labels_train, parameters, svm.SVC(), is_little_data=False)
    clf = svm.SVC(kernel="linear", C=32)
    clf.fit(features_train, labels_train)
    # print("C_best:", clf.best_estimator_.C)
    print("fit used", round(time() - t, 3), "s")
    print("svm linear C=32:", clf.score(features_test, labels_test))
    # show_image(clf, features_test, labels_test)

    parameters = {'kernel': ['rbf'], 'C': range(7900, 8000)}
    t = time()
    # clf = find_best_estimator(features_train, labels_train, parameters, svm.SVC(), is_little_data=False)
    clf = svm.SVC(C=38999989)
    clf.fit(features_train, labels_train)
    # print("C_best:", clf.best_estimator_.C)
    print("fit used", round(time() - t, 3), "s")
    print("svm rbf C=38999989:", clf.score(features_test, labels_test))
    # show_image(clf, features_test, labels_test)

    # parameters = {'min_samples_split': range(15, 20)}
    t = time()
    # clf = find_best_estimator(features_train, labels_train, parameters, tree.DecisionTreeClassifier(),is_little_data=False)
    clf = tree.DecisionTreeClassifier(min_samples_split=18)
    clf.fit(features_train, labels_train)
    print("fit used", round(time() - t, 3), "s")
    print("DecisionTreeClassifier min_samples_split=18:", clf.score(features_test, labels_test))
    # show_image(clf, features_test, labels_test)

    parameters = {'weights': ['uniform', 'distance'], 'n_neighbors': range(5, 10)}
    t = time()
    # clf = find_best_estimator(features_train, labels_train, parameters, KNeighborsClassifier(),is_little_data=False)
    clf = KNeighborsClassifier(n_jobs=-1, n_neighbors=8)
    clf.fit(features_train, labels_train)
    print("fit used", round(time() - t, 3), "s")
    print("KNeighborsClassifier n_neighbors=7:", clf.score(features_test, labels_test))
    # show_image(clf, features_test, labels_test)

    parameters = {'base_estimator': [GaussianNB(), svm.SVC(kernel='linear'), svm.SVC(kernel='rbf'),
                                     tree.DecisionTreeClassifier()], 'n_estimators': range(1, 100),
                  'algorithm': ['SAMME']}
    parameters1 = {'n_estimators': range(1, 10000)}
    t = time()
    # clf = find_best_estimator(features_train, labels_train, parameters, AdaBoostClassifier(),is_little_data=False)
    clf = AdaBoostClassifier()
    clf.fit(features_train, labels_train)
    print("fit used", round(time() - t, 3), "s")
    print("AdaBoostClassifier:", clf.score(features_test, labels_test))
    # show_image(clf, features_test, labels_test)

    parameters = {'n_estimators': range(4, 100), 'min_samples_split': range(6, 100)}
    t = time()
    # clf = find_best_estimator(features_train, labels_train, parameters, RandomForestClassifier(),is_little_data=False)
    clf = RandomForestClassifier(n_estimators=11, min_samples_split=10)
    clf.fit(features_train, labels_train)
    print("fit used", round(time() - t, 3), "s")
    print("RandomForestClassifier n_estimators=11 min_samples_split=10:", clf.score(features_test, labels_test))
    show_image(clf, features_test, labels_test)
