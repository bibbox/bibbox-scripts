#!/usr/bin/env python

import os
import sys
import getopt
import shutil
import json

from pprint import pprint

def createFolders(instancepath, folder):
    directory = instancepath + "/" + folder
    print("Creating folders: " + directory)
    if not os.path.exists(directory):
        os.makedirs(directory)

def copyFiles(applicationpath, source, instancepath, destination):
    try:
        print("Copy file: " + destination)
        src = applicationpath + "/" + source
        dest = instancepath + "/" + destination
        shutil.copy2(src, dest)
    except:
        print("Unexpected copy error:" + str(sys.exc_info()[1]))

argv = sys.argv[1:]
opts, args = getopt.getopt(argv,"a:i:",["applicationpath=","instancepath="])
for opt, arg in opts:
    if opt == '-h':
        print('test.py -a <applicationpath> -i <instancepath>')
        sys.exit()
    elif opt in ("-a", "--applicationpath"):
        applicationpath = arg
    elif opt in ("-i", "--instancepath"):
        instancepath = arg

dir = os.path.dirname(os.path.realpath(__file__))
applicationfiles = os.path.join(dir, 'config/applicationfiles.json')

with open(applicationfiles) as data_file:
    applicationfiles_json = json.load(data_file)

with open(applicationpath + '/file_structure.json') as data_file:
    file_structure_json = json.load(data_file)

print("----------------")
for folder in file_structure_json["makefolders"]:
    createFolders(instancepath, folder)
print("----------------")
for folder in file_structure_json["copyfiles"]:
    copyFiles(applicationpath, folder['source'], instancepath, folder['destination'])
print("----------------")
for folder in applicationfiles_json["copyapplicationfiles"]:
    copyFiles(applicationpath, folder['source'], instancepath, folder['destination'])