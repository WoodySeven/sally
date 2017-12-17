#!/usr/bin/env python
import os
def crawl_dirname():
    path="D:\android-sdk_r25.2.5-windows"
    list=os.listdir(path)
    print(list)
    fp=open("myfile.txt","wb")
    for i in list:
        fp.write("{}\n".format(i).encode("utf-8"))
    fp.close()
    abspath=os.path.abspath("myfile.txt")
    print(abspath)
    return

crawl_dirname()