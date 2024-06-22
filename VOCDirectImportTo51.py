#%%
'''
Read in a set of images and annotations in VOC format, and ingest to 51.

This applies specifically to the WOTR dataset.

Using the 'tf' conda environment
'''

# import os,shutil,datetime
# import glob
# import json
# import xml.etree.cElementTree as ET

# from re import X
# from numpy import empty
# from pyparsing import disable_diag
# import xml.etree.cElementTree as ET

import json
import os
# import random
# from PIL import Image
# import sys

import fiftyone as fo

from utils.fileOps import *
# from plusCoco import *
#from readSynth import *

vocInputBaseFP = "/media/pg/Expansion/data/WOTR/"
annosFP = os.path.join(vocInputBaseFP,"Annotations")
imagesFP = os.path.join(vocInputBaseFP,"JPEGImages")
dsName = 'WOTR'
dataset_type = fo.types.VOCDetectionDataset

'loaded'
#%%

def delete51DS(dbName):
    if fo.dataset_exists(dbName):
        print("deleting existing",dbName)
        fo.delete_dataset(dbName)

delete51DS(dsName)

# VOCdataset = fo.utils.voc.VOCDetectionDatasetImporter(
#     dataset_dir=vocInputBaseFP,
#     data_path='JPEGImages/',
#     labels_path= 'Annotations/',
#     include_all_data=False,
#     extra_attrs=True,
#     shuffle=True,
#     seed=None,
#     max_samples=None,
# )
'done'
#%%

#%%



# CLASS fiftyone.utils.voc.VOCDetectionDatasetImporter(dataset_dir=None, data_path=None, labels_path=None, include_all_data=False, extra_attrs=True, shuffle=False, seed=None, max_samples=None)

# This doesn't work - wants a 'data' folder, then doesn't ingest anything

# Rename Annotations to data

dataset_type = fo.types.VOCDetectionDataset
dataset = fo.Dataset.from_dir(
    dataset_dir=vocInputBaseFP,
    data_path='JPEGImages/',
    labels_path= 'Annotations/',
    dataset_type=dataset_type,
    name=dsName,
)
print("and make persistent")
dataset.persistent = True
'ds available'

#%%

print(dataset)
# print(dataset.head())

#%%

fo.pprint(dataset.stats(include_media=True))





#%%

dataset.classes

#%%


#%%