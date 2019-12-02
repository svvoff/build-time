import sys
import os
import errno
import time
from datetime import datetime
import csv
import argparse
from os.path import expanduser

csv_file_name = 'log.csv'
home = expanduser("~")
path = home + "/build_time/"
filepath = path + csv_file_name
timefile = ".time"
timepath = path + timefile

if not os.path.exists(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise e

if 'start' in sys.argv:
    f = open(timepath, "w+")
    seconds = str(time.time())
    f.write(seconds)
    f.close()
else:
    f = open(timepath, "r")
    val = float(f.read())
    f.close()
    build_time = time.time() - val

    date = datetime.now().replace(microsecond=0).isoformat(" ")

    is_csv_new = False
    if os.path.isfile(filepath) == False:
        f = open(filepath, "w+")
        f.close()
        is_csv_new = True

    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default='unknown')
    args = parser.parse_args()
    productname = args.name
    with open(filepath, 'a') as log:
        fieldnames = ['date', 'build_time', "product_name"]
        writer = csv.DictWriter(log, fieldnames=fieldnames)
        if is_csv_new:
            writer.writeheader()
        writer.writerow({'date': date, 'build_time': build_time, "product_name" : productname})
