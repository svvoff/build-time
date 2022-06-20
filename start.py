#!/usr/local/bin/python3

import os
import csv
from constants import *

def write_csv(date, time, project_name, filename, tag = None):
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        # checks if file exists
        print ("File exists and is readable")
    else:
        print ("Either file is missing or is not readable, creating file...")
        file = open(filename, 'w+')
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        file.close()

    with open(filename,'a') as file:
        r = {
            'date' : date,
            'project' : project_name,
            'start' : time,
        }
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(r)

write_csv(date_str, now_time, project_name, file_path)
