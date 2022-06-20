import os
import time
from datetime import date

build_time_file_name = "build_time.csv"
fieldnames = ['date', 'project', 'start', 'end', 'tag']
environ = os.environ

project_name = "stub"
try:
   project_name = environ['XcodeWorkspace']
except KeyError: 
    print("Environment variable does not exist")

now_time = time.time()
date_str = str(date.today())

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = dir_path + "/" + build_time_file_name