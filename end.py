#!/usr/local/bin/python3

import os
from constants import *
import csv

def write_csv(time, filename, tag = None):
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        # checks if file exists
        print ("File exists and is readable")
    else:
        print ("Either file is missing or is not readable, creating file...")
        f = open(filename, 'w+')
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        f.close()

    with open(filename,'r+') as file:
        lines = len(file.readlines())
        if lines > 1:
            with open(filename,'r+') as csv_file:
                reader = csv.DictReader(csv_file)
                r = None
                row_index = 0
                last_row_index = lines - 1
                tmp_filename = filename + 'tmp'
                with open(tmp_filename, 'w+') as write_file:
                    writer = csv.DictWriter(write_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in reader:
                        row_index += 1
                        if row:  # avoid blank lines
                            if row_index is last_row_index:
                                r = row
                                r['tag'] = tag
                                r['end'] = time
                                writer.writerow(r)
                            else:
                                writer.writerow(row)
            os.remove(file_path)
            os.rename(tmp_filename, file_path)
        else:
            print("something ")