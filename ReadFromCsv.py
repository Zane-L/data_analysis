import csv
import datetime
import pandas as pd
import numpy as np
from pandas import DataFrame


# start = datetime.datetime.now()
# length = 0
# list1 = []
#
# # load csv file through csv module
# with open("test.csv", 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     # takes about 1.2s to convert to a list from csv file with 100w pieces of data
#     list1 = list(reader)
#     length = len(list1)
# end = datetime.datetime.now()
# print(start, end, end-start, length)
# print(list1[10824])

# load csv file through pandas module

# used to store the data in each group
# every group's data will be a tuple. exp: [(group1),(group2),(group3)...]
data_from_every_group = []

start = datetime.datetime.now()

df = pd.read_csv("test.csv")  # df will be of DataFrame type
# group_by_name_and_state = df.groupby(["name", "state"])
# group_by_name_and_state.get_group(('lisi', 'sleep'))
group_by_name = df.groupby(["name"])

# get group ID(name for every group)
# exp:Index(['lisi', 'wangwu', 'zhangsan'], dtype='object', name='name')
names = group_by_name.size().index
for i in range(len(group_by_name.count())):
    data_from_every_group.append(group_by_name.get_group(names[i]))
# lisi = names[0]
list3 = []  # temporary list
list4 = []  # temporary list

# information for every one, storing date and state in every period about someone
# exp:
# [('name1', [['start_time', 'end_time', 'state', duration],...]),
# ('name1', [['start_time', 'end_time', 'state', duration],...]),....]
list5 = []

# storing name,state and total time for every status
# exp:
# [('name', [['category', 'duration'],....]),('name', [['category', 'duration'],....]),...]
list6 = []
for idx in range(len(data_from_every_group)):
    for i in range(len(data_from_every_group[idx])):
        if len(list3) == 0:
            start_time = data_from_every_group[idx].iloc[i, 0]
            list3.append(start_time)
        # if i is the last or ith state not equal to (i+1)th state
        if i == len(data_from_every_group[idx])-1 or data_from_every_group[idx].iloc[i+1, 2] != data_from_every_group[idx].iloc[i, 2]:
            end_time = data_from_every_group[idx].iloc[i, 0]
            state = data_from_every_group[idx].iloc[i, 2]
            list3.append(end_time)
            list3.append(state)
            d1 = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f')
            d2 = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S.%f')
            # if 0 == (d2-d1).microseconds:
            #     list3.append(str(d2 - d1)+".00")
            # else:
            #     list3.append(str(d2 - d1))
            list3.append(float(("%.3f" % (d2 - d1).total_seconds())))
            list4.append(list3)
            list3 = []
    list5.append((names[idx], list4))
    list4 = []

for i in range(len(list5)):
    df1 = DataFrame(list5[i][1], columns=['start_time', 'end_time', 'state', 'total_time'])
    group_by_state = df1.groupby(['state'])
    state_list = group_by_state.size().index  #
    list6.append((list5[i][0], []))
    for j in range(len(state_list)):
        time_sum = ("%.3f" % group_by_state.get_group(state_list[j])["total_time"].sum())
        list6[i][1].append([state_list[j], time_sum])

end = datetime.datetime.now()

print(end-start)










# group_by_name.count()
#           date  state
# name
# lisi        37     37
# wangwu      30     30
# zhangsan    33     33

# len(group_by_name.count())
# 3
# group_by_name.size().values
# array([37, 30, 33])
# group_by_name.size().index
# Index(['lisi', 'wangwu', 'zhangsan'], dtype='object', name='name')


# a = DataFrame(list5)
# a
#           0                                                  1
# 0      lisi  [[2020-10-29 21:04:04.893489, 2020-10-29 21:04...
# 1    wangwu  [[2020-10-29 21:04:06.895115, 2020-10-29 21:04...
# 2  zhangsan  [[2020-10-29 21:04:05.894608, 2020-10-29 21:04...

# [float(i[3]) for i in a.iloc[0][1]]
# [3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 2.0, 0.0, 0.0, 0.0, 10.01, 4.0, 0.0, 0.0, 0.0, 6.01, 0.0, 1.01]
# sum([float(i[3]) for i in a.iloc[0][1]])
# 29.029999999999998

# ("%.3f" % gbs.get_group('play')["total_time"].sum())