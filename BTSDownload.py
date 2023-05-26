#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:54:09 2023

@author: aidencamilleri
"""

import requests
import certifi

baseURL = 'https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_'

for i in range(1987, 2023): #grab years from 1987-2022
    for j in range(1, 13): #grab months from Jan.-Dec.
        specificURL = baseURL + str(i) + '_' + str(j) + ".zip" #add year and month to make full URL
        response = requests.get(specificURL, stream=True) #get file from specified web address
        filename = "BTS_" + str(j) + '_' + str(i) + ".zip" #make filename from year and month
        with open(filename, "wb") as f:
            f.write(response.content) #write it to a file