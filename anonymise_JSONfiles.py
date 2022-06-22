# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:50:46 2022

@author: mhnazaee
"""

import json
# import os
import glob
  
# Opening JSON file
filename_root= "Z:\\Percept Data Medtronic\\"

# subfolders = [ f.path for f in os.scandir(filename_root) if f.is_dir() ]
# [glob.glob(f+"\\*.json") for f in subfolders]

subfolders=glob.glob("Z:\\Percept Data Medtronic\\**", recursive = True)
json_files_temp=[ f for f in subfolders if ".json" in f] 
json_files=[ f for f in json_files_temp if "copy" not in f] 


for f in json_files:
    f_temp = open(f)
    # returns JSON object as 
    # a dictionary
    data = json.load(f_temp)
    name_json=f.split('\\')
    Initials_patient=name_json[2]
    # data['PatientInformation']=[]
    if data['PatientInformation']['Final']['PatientFirstName']:
        Initials_patient=data['PatientInformation']['Final']['PatientFirstName'][0]+data['PatientInformation']['Final']['PatientLastName'][0]
        
        data['PatientInformation']['Final']['PatientFirstName']=data['PatientInformation']['Final']['PatientFirstName'][0]
        data['PatientInformation']['Final']['PatientLastName']=data['PatientInformation']['Final']['PatientLastName'][0]
        
        if data['PatientInformation']['Initial']['PatientFirstName']:
            data['PatientInformation']['Initial']['PatientFirstName']=data['PatientInformation']['Initial']['PatientFirstName'][0]
            data['PatientInformation']['Initial']['PatientLastName']=data['PatientInformation']['Initial']['PatientLastName'][0]

        
    jsonString = json.dumps(data)
    jsonFile = open("Z:\\Percept Data Medtronic\\anonymised_JSONfiles\\anon" + Initials_patient + "_" + name_json[-1], 'w')
    jsonFile.write(jsonString)
    jsonFile.close()
        

    # Closing file
    f_temp.close()




