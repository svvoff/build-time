import os
import time
from datetime import date, datetime

build_time_file_name_tail = "build_time.csv"
fieldnames = ['date', 'project', 'start', 'end', 'tag']
environ = os.environ

project_name = "stub"
try:
   project_name = environ['XcodeWorkspace']
except KeyError:
    try:
        project_name = environ['XcodeProject']
    except:
        print("Environment variable does not exist")

project_name = project_name.replace(" ", "_")

def file_name_with_project_name(p_n):
    return p_n + build_time_file_name_tail

build_time_file_name = file_name_with_project_name(project_name)

now_time = time.time()
date_str = str(date.today())

dir_path = os.path.dirname(os.path.realpath(__file__))

def file_path_with_file_name(f_n):
    return dir_path + "/" + f_n

file_path = file_path_with_file_name(build_time_file_name)

def log_error(error):
    log_path = file_path_with_file_name('log.txt')
    with open(log_path, 'a+') as file:
        now = datetime.now()
        date_str = now.strftime("%d.%m.%Y, %H:%M:%S")
        file.write("\n" + date_str + " " + project_name + " " + error)

