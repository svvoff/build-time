import numpy as np
import matplotlib.pyplot as plt
import csv
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--input')
parser.add_argument('--product')
args = parser.parse_args()
input_file = args.input
print(args)
product_name = args.product

class BuildTime:
    def __init__(self, date, time):
        self.date = date
        self.time = float(time)

class Project:
    def __init__(self, name):
        self.values = []
        self.splited = {}
        self.prepared = False
        self.name = name

    def addBildTime(self, buildTime):
        self.values.append(buildTime)
    
    def prepareData(self):
        if self.prepared:
            return
        for value in self.values:
            time_list = self.splited.get(value.date)
            if time_list is None:
                time_list = []
            time_list.append(value.time)
            self.splited[value.date] = time_list
        self.prepared = True


projects = []

def get_project(name):
    for project in projects:
        if project.name == name:
            return project
    return None

datetime_format = '%Y-%m-%d %H:%M:%S'
date_format = '%Y-%m-%d'

with open(input_file, 'r') as log:
    fieldnames = ['date', 'build_time', "product_name"]
    reader = csv.DictReader(log, fieldnames=fieldnames)
    for row in reader:
        time=row["build_time"]
            
        if time == "build_time":
            continue
        project = get_project(row["product_name"])
        date = datetime.strptime(row["date"], datetime_format).strftime(date_format)
        build_time = BuildTime(date=date, time=time)
        if project is None:
            project = Project(row["product_name"])
            projects.append(project)
        project.addBildTime(build_time)

for project in projects:
    project.prepareData()     

project = get_project(product_name)
if project is None:
    raise

dates = project.splited.keys()
# datetime.strptime(date_time_str, '%Y-%m-%d')
dates = sorted(dates, key=lambda x: datetime.strptime(x, date_format))
dates = np.array(dates)
# dates_without_time = map(lambda x: datetime.strptime(x, datetime_format).strftime("%Y-%m-%d"), dates)
# dates_without_time = sorted(dates_without_time, key=lambda x: datetime.strptime(x, "%Y-%m-%d"))

# indexes = np.array(range(0, len(dates)))
indexes = range(0, len(dates))

sums=[]

for v in dates:
    
    summed = sum(project.splited[v])
    summed /= 60
    sums.append(summed)
# sums = np.array(sums)

fig = plt.figure()
ax = fig.add_subplot(111)

plt.xticks(indexes, dates, rotation='vertical')
# plt.plot(indexes, sums)
plt.stem(indexes, sums)

# plt.bar(indexes, sums)

plt.xlabel('date')
plt.ylabel('build time in minutes')
plt.subplots_adjust(bottom=0.25)

plt.title("Build time")

for i, v in enumerate(sums):
    ax.text(i, v+1, "%d" %v, ha="center")

# plt.legend()

plt.show()