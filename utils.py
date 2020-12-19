# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:38:38 2019
@title : set of support tool
@author: Giovanni Licitra
@emmail: gianni.licitra7@gmail.com
"""


from zipfile import ZipFile
from urllib.request import urlretrieve
import os
import pathlib

# set root directory
def set_root():
    """Set root directory"""
    path_root = pathlib.Path("C:/Users/giann/data-science-core")
    os.chdir(path_root)
    print(f'- root directory = {os.getcwd()}')

def download_dataset(url) :
    """ 
    Download dataset from UCI web site into the folder ./dataset/. 
    The function can handle zip file. 
      
    Attributes: 
        url (str): url where it is located the repository
        
    Example:
        >>> download_dataset('http://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip')
    """
    
    set_root()
    path_dataset = pathlib.Path.cwd() / 'dataset'
    
    url_OS = pathlib.Path(url) # tailor path w.r.t. OS
    format_file = url_OS.suffix # get format e.g. .zip, .csv, etc...
    folder_name = url_OS.stem.lower() # .lower() remove capital letter
    
    # Create target Directory if don't exist
    if not os.path.exists(path_dataset / folder_name):
        os.mkdir(path_dataset / folder_name)
        print("- directory " , path_dataset / folder_name,  " Created ")
    else:    
        print("- directory " , path_dataset / folder_name,  " already exists")
    
    # download file from web
    print('- downloading file...', end = ' ')
    file_name = path_dataset / folder_name / str('dataset' + format_file)      
    urlretrieve(url, file_name)
    print('Done!')
    
    # Unzip file if the repository is an archive
    if format_file == '.zip' :
        with ZipFile(file_name, 'r') as zipObj:
           # Extract all the contents of zip file in current directory
           zipObj.extractall(path_dataset / folder_name)
        # delete zip file 
        os.remove(file_name)
    
    print(f'- content in folder: {folder_name}')
    print(f"- list of files : {os.listdir(path_dataset / folder_name)}")
