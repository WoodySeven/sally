#!/usr/bin/env python
#encoding: utf-8
import os


def crawl_path(path):
    """
    1.确定要遍历的目录是否存在
    2.爬取指定目录，生成一个list
    3.打开文件，写入数据
    4.返回myfile.txt所在的路径。
    """
    myfile = "myfile.txt"
    if not os.path.exists(path):
        print("Error: 文件或目录不存在")
        return
    if os.path.isfile(path):
        print("Error: 不能是文件")
        return
    list_path = os.listdir(path)
    with open("myfile.txt", 'wb')  as fp:
        fp.write("\n".join(list_path).encode("utf-8"))
        #这句的意思是遍历完成后一次全部打印
    return myfile


def usage():
    print("please input path")
    print("eg. crwaler_path.py path_name")


if __name__ == "__main__":
    """
    这个程序应该接受如下的调用方式：crwaler_path.py  路径名
    把这个路径下面所有的目录或文件写入到myfile.txt
    """
    # crawl_path(r"D:\android-sdk_r25.2.5-windows")
    # crawl_path(r"D:\android")
    # crawl_path(r"F:\GitHub\autotest7\lesson2\crawler.py")
    import sys
    if len(sys.argv) != 2:
        usage()
        exit(0)
    path = sys.argv[1]
    crawl_path(path)
