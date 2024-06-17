#%%

from cmath import isnan
import os,glob
import datetime
import json
import csv
import math
import numpy as np

def test():
    print("test")
    
def removeFilesFromFolder(fp):
    #print("removeFilesFromFolder",fp)
    files = glob.glob(fp+"/*")
    for f in files:
        if os.path.isdir(f):
            #print("recursing on",f)
            removeFilesFromFolder(f)
            os.rmdir(f)
        else:
            #print("removing file",f)
            os.remove(f)

def ensureFolder(fp):
    if not os.path.exists(fp):
        os.mkdir(fp)

def ensureFolderClean(fp):
    ensureFolder(fp)
    removeFilesFromFolder(fp)

def getCurrentDataFolder(baseFP):
    mydir = os.path.join(baseFP, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    os.makedirs(mydir)
    return mydir


##################
# Read JSON file
##################
def getJsonFromFile(fpath):
    assert(os.path.isfile(fpath))
    with open(fpath) as f:
        # hmmm, not dumping correct json from the C++
        # 0. is not allowed, should be 0.0
        # and others...
        aStr = f.read()
        aStr = aStr.replace("null","0.0")
        aStr = aStr.replace(".Inf","0.0")
        aStr = aStr.replace("Infinity","0.0")
        aStr = aStr.replace(". ",".0")
        aStr = aStr.replace(".\n",".0\n")
        aStr = aStr.replace(".,",".0,")
        #print(aStr)
        oJ = json.loads(aStr)
        # print(oJ)

        return oJ

#%%



#%%
