#%%
'''
Read in a set of images and annotations in VOC format, and ingest to 51.

This applies specifically to the WOTR dataset.

Using the 'tf' conda environment
'''

import os,shutil,datetime
import glob
import json
import xml.etree.cElementTree as ET

from re import X
from numpy import empty
from pyparsing import disable_diag
import xml.etree.cElementTree as ET

import json
import os
import random
from PIL import Image
import sys

import fiftyone as fo

from utils.fileOps import *
# from plusCoco import *
#from readSynth import *

vocInputBaseFP = "/media/pg/Expansion/data/WOTR/"
annosFP = os.path.join(vocInputBaseFP,"Annotations")
imagesFP = os.path.join(vocInputBaseFP,"JPEGImages")

'loaded'
#%%

'''
This doesn't work - wants a 'data' folder, then doesn't ingest anything

dataset_type = fo.types.VOCDetectionDataset
dataset = fo.Dataset.from_dir(
    dataset_dir=vocInputBaseFP,
    dataset_type=dataset_type,
    name=dsName,
)
'''
'ds available'

#%%

imgWidth,imgHeight = 640.0,480.0        # actually read for each image
# minimum size requirement for an object
minSize = 5 #pixels = both directions

srcClassTarget = "reflective_cone"
tgtClass = "safety_cone"

def ingestVOC(dsName):


    if fo.dataset_exists(dsName):
        print("deleting existing",dsName)
        fo.delete_dataset(dsName)

    srchStr = annosFP+"/"+"*.xml"
    filelist = glob.glob(srchStr)
    print("length of filelist",len(filelist))


    samples51 = []
    classes = []
    cntCones = 0
    iDone = 0

    for annoFP in filelist:
        xmlFN = os.path.basename(annoFP)
        xmlFP = annoFP
        baseFN = os.path.splitext(os.path.basename(annoFP))[0]
        imgFN = baseFN+".jpg"
        imgFP = os.path.join(imagesFP,imgFN)
        assert(os.path.exists(xmlFP))
        assert(os.path.exists(imgFP))

        if True:    # iDone==0:
            # assume all images the same size...
            im = Image.open(imgFP)
            imgWidth, imgHeight = im.size
            imgWidth = float(imgWidth)
            imgHeight = float(imgHeight)
            # print("sample image:",imgFP)
            # print("image size:",imgWidth,imgHeight)




        # parse the xml file
        tree = ET.parse(xmlFP)
        root = tree.getroot() 
  
    # iterate news items 
        detections = []
        hasCone = False
        for obj in root.findall('./object'): 
            label = obj.find('name').text

            if label == srcClassTarget:
                bndbox = obj.find('bndbox') 
                xmin = float(bndbox.find('xmin').text)
                ymin = float(bndbox.find('ymin').text)
                xmax = float(bndbox.find('xmax').text)
                ymax = float(bndbox.find('ymax').text)

                preBBox = [xmin, ymin, xmax, ymax]

                xmin = xmin / imgWidth
                ymin = ymin / imgHeight
                xmax = xmax / imgWidth
                ymax = ymax / imgHeight

                width = xmax - xmin
                height = ymax - ymin

                # [0,1] normalized format


                bounding_box = [xmin, ymin, width, height]

                # minimum size requirement

                if width > (minSize/imgWidth) and height > (minSize/imgHeight):
                    detections.append(
                        # save with target class
                        fo.Detection(label=tgtClass, bounding_box=bounding_box)
                    )
                else:
                    print("skipping ",label,bounding_box,preBBox)
                # print("added:",label,bounding_box,preBBox)

                if label not in classes:
                    classes.append(label)
                if label == "reflective_cone":
                    hasCone = True

        # Store detections in a field name of your choice

        if hasCone:
            cntCones += 1
            sample51 = fo.Sample(filepath=imgFP)
            sample51["ground_truth"] = fo.Detections(detections=detections)
            samples51.append(sample51)

        iDone += 1
        if iDone % 100 == 0:
            print("done",iDone)

        if iDone > 100000:
            break
        # if iDone > 100:
        #     break

    # Create dataset
    print("creating dataset with #",iDone)
    dataset = fo.Dataset(dsName)
    print("with #",len(samples51))
    dataset.add_samples(samples51)
    print("built")


    print("classes",classes)
    print("cntCones",cntCones)

        


dsName = "WOTR-cones"

ingestVOC(dsName)
'done'

#%%













#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%