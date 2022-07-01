#!/usr/local/bin/python3

import os
from constants import *
import csv

log_error("run end.py")

def write_csv(time, filename, tag = None):
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        # checks if file exists
        error_str = "open file " + filename + " is ok"
        log_error(error_str)
        print ("File exists and is readable")
    else:
        print ("Either file is missing or is not readable, creating file...")
        error_str = "end.py create new file " + filename
        log_error(error_str)

        f = open(filename, 'w+')
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        f.close()
    
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
            lines = filter(lambda x: x.strip(), lines)
            filehandle.writelines(lines) 

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
                            if row_index == last_row_index:
                                r = row
                                r['tag'] = tag
                                r['end'] = time
                                writer.writerow(r)
                            else:
                                log_error("end.py log row at index: " + str(row_index) + " last_row_index " + str(last_row_index) + " row " + str(row))
                                writer.writerow(row)
            os.remove(file_path)
            os.rename(tmp_filename, file_path)
        else:
            print("something ")