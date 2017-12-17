#!/usr/bin/env python
def read():
    fp=open("name.txt","rb")
    content=fp.readlines()
    print(content)
    for i in content:
        print(i.decode("utf-8").strip())
    fp.close()

def write():
     fp=open("test.txt","wb")
     address=["中国","非洲","日本"]
     for i in address:
         fp.write("{}\n".format(i).encode("utf-8"))
     fp.close()

write()
