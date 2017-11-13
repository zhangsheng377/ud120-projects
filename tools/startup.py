#!/usr/bin/python

print()
print("checking for nltk")
try:
    import nltk
except ImportError:
    print("you should install nltk before continuing")

print("checking for numpy")
try:
    import numpy
except ImportError:
    print("you should install numpy before continuing")

print("checking for scipy")
try:
    import scipy
except:
    print("you should install scipy before continuing")

print("checking for sklearn")
try:
    import sklearn
except:
    print("you should install sklearn before continuing")

print()
print("downloading the Enron dataset (this may take a while)")
print("to check on progress, you can cd up one level, then execute <ls -lthr>")
print("Enron dataset should be last item on the list, along with its current size")
print("download will complete at about 423 MB")
import urllib.request


def report_hook(blocks_read, block_size, total_size):
    if not blocks_read:
        print("Connection opened")
    if total_size < 0:
        print("Read %d blocks" % blocks_read)
    else:
        print("downloading: %d KB, totalsize: %d KB" % (blocks_read * block_size / 1024.0, total_size / 1024.0))


url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
urllib.request.urlretrieve(url, filename="../enron_mail_20150507.tar.gz", reporthook=report_hook)
print("download complete!")

print()
print("unzipping Enron dataset (this may take a while)")
import tarfile
import os

os.chdir("..")
tfile = tarfile.open("enron_mail_20150507.tar.gz", "r:gz")
tfile.extractall(".")

print("you're ready to go!")
