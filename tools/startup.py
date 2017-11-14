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

print("checking for urllib.request")
try:
    import urllib.request
except:
    print("you should install urllib before continuing")

print("checking for requests")
try:
    import requests
except:
    print("you should install requests before continuing")

print("checking for contextlib")
try:
    import contextlib
except:
    print("you should install contextlib before continuing")

print("checking for tarfile")
try:
    import tarfile
except:
    print("you should install tarfile before continuing")

print("checking for os")
try:
    import os
except:
    print("you should install os before continuing")

print()
print("downloading the Enron dataset (this may take a while)")
print("to check on progress, you can cd up one level, then execute <ls -lthr>")
print("Enron dataset should be last item on the list, along with its current size")
print("download will complete at about 423 MB")

url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
try:
    import urllib.request


    def report_hook(blocks_read, block_size, total_size):
        if not blocks_read:
            print("Connection opened")
        if total_size < 0:
            print("Read %d blocks" % blocks_read)
        else:
            print("downloading: %d KB, totalsize: %d KB" % (blocks_read * block_size / 1024.0, total_size / 1024.0))


    urllib.request.urlretrieve(url, filename="../enron_mail_20150507.tar.gz", reporthook=report_hook)
except:
    import requests

    proxies = {
        "http": "http://127.0.0.1:8087",
        "https": "http://127.0.0.1:8087"
    }
    from contextlib import closing

    with closing(requests.get(url, proxies=proxies, stream=True)) as response:
        chunk_size = 1024
        content_size = int(response.headers['content-length'])
        data_length = 0
        with open("../enron_mail_20150507.tar.gz", "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                data_length += len(data)
                print("downloaded:", int(data_length / 1024), " KB    total_size:", int(content_size / 1024), " KB    ",
                      data_length * 1.0 / content_size, " %")
print("download complete!")

print()
print("unzipping Enron dataset (this may take a while)")
import tarfile
import os

os.chdir("..")
with tarfile.open("enron_mail_20150507.tar.gz", "r") as tarball:
    def track_progress(members, files_num):
        index = 0
        for member in members:
            index += 1
            print("tarfile index:", index, "    total_file_num:", files_num, "    ", index * 1.0 / files_num, " %")
            yield member


    files_num = len(tarball.getmembers())
    tarball.extractall(path=".", members=track_progress(tarball, files_num))

print("you're ready to go!")
