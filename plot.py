#!/usr/local/bin/python3

import csv
from constants import *
import matplotlib.pyplot as plt
import argparse

# plt.style.use('_mpl-gallery')

parser = argparse.ArgumentParser()
parser.add_argument('--project')
args = parser.parse_args()
project_name = args.project

if project_name is None:
    raise '--project arg is empty'

daily_build_time = 'daily_build_time'
daily_success_time = 'daily_success_time'
daily_failed_time = 'daily_failed_time'

def modify_row_by_tag(data, row):
    start = int(float(row['start']))
    end = int(float(row['end']))
    diff = end - start
    if diff > 0:
        if row.get('tag') == 'success':
            if data.get(daily_success_time):
                dst = int(data.get(daily_success_time))
                dst += diff
                data[daily_success_time] = dst
            else:
                data[daily_success_time] = diff
        elif row.get('tag') == 'fail':
            if data.get(daily_failed_time):
                dft = int(data.get(daily_failed_time))
                dft += diff
                data[daily_failed_time] = dft
            else:
                data[daily_failed_time] = diff
    return data 

def collect_data(file_name):
    with open(file_name, 'r+') as csv_file:
        reader = csv.DictReader(csv_file)
        data_dict = {}
        for row in reader:
            if row.get('project') == project_name:
                end = row['end']
                if end:
                    start = row['start']
                    if start:
                        date_object = row['date']
                        if data_dict.get(date_object):
                            tmp = data_dict.get(date_object)
                            tmp.append(row)
                        else:
                            tmp = [row]
                            data_dict[date_object] = tmp
        if data_dict:
            c_d = {}
            for i, (k, v) in enumerate(data_dict.items()):
                for row in v:
                    start = int(float(row['start']))
                    end = int(float(row['end']))
                    diff = end - start
                    if diff > 0:
                        if c_d.get(k):
                            dd = c_d.get(k)
                            t = int(dd.get(daily_build_time))
                            t += diff
                            dd[daily_build_time] = t
                            modify_row_by_tag(dd, row)
                            c_d[k] = dd
                        else:
                            dd = {}
                            dd[daily_build_time] = diff
                            modify_row_by_tag(dd, row)
                            c_d[k] = dd
                    
            return c_d
        else:
            raise ValueError('No data for project = ' + project_name)
    return None

char_data = collect_data(file_path)
# print(char_data)

# make data
def apply_common(x):
    date = x[0]
    time = x[1].get(daily_build_time)
    return (date, time)

def apply_success(x):
    date = x[0]
    time = x[1].get(daily_success_time)
    return (date, time)

def apply_fail(x):
    date = x[0]
    time = x[1].get(daily_failed_time)
    return (date, time)

build_common = list(map(apply_common, char_data.items()))
build_success = list(map(apply_success, char_data.items()))
build_fail = list(map(apply_fail, char_data.items()))

def common_x(x):
    return x[0]

def common_y(x):
    seconds = int(x[1])
    return seconds / 60

x_common = list(map(common_x, build_common))
y_common = list(map(common_y, build_common))

x_success = list(map(common_x, build_success))
y_success = list(map(common_y, build_success))

x_fail = list(map(common_x, build_fail))
y_fail = list(map(common_y, build_fail))

# plot
fig, ax = plt.subplots()

ax.plot(x_common, y_common, linewidth=2, markersize=5, marker='.', alpha=0.5)
ax.plot(x_success, y_success, linewidth=2, markersize=10, marker='+', alpha=0.5, color='green')
ax.plot(x_fail, y_fail, linewidth=2, markersize=10, marker='x', alpha=0.5, color='red')

for i,j in zip(x_common,y_common):
    ax.annotate(str(round(j, 2)),  xy=(i, j),
                horizontalalignment='center',
                verticalalignment='center')

for i,j in zip(x_success,y_success):
    ax.annotate(str(round(j, 2)),  xy=(i, j), color='green',
                weight='heavy',
                horizontalalignment='center',
                verticalalignment='center')

for i,j in zip(x_fail,y_fail):
    ax.annotate(str(round(j, 2)),  xy=(i, j), color='red',
                weight='heavy',
                horizontalalignment='center',
                verticalalignment='center')

# for i,j in zip(x,y):
#     ax.annotate(str(j),  xy=(i, j), color='white',
#                 fontsize="large", weight='heavy',
#                 horizontalalignment='center',
#                 verticalalignment='center')

plt.show()