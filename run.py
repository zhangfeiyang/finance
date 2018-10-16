#!/usr/bin/python
import os

def get_all_files(dirname,files):
   
    try:
        dirs = os.listdir(dirname)

        for dir in dirs:
              get_all_files(dir,files)
    #except NotADirectoryError:
    except:
        files.append(dirname)

if __name__=="__main__":
   
    index_file = open('index','r')
    indexs = index_file.read().split()



    #files = []
    #get_all_files('.',files)
    #for file in files:
    #    print(file)
