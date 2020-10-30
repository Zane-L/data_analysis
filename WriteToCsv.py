import csv
import time
import random
import datetime

name = ["zhangsan", "lisi", "wangwu"]
state = ["sleep", "play", "study"]

# 格式化成2016-03-20 11:45:39形式
# print(time.localtime())
# Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

start = datetime.datetime.now()

with open("test.csv", 'w') as csvfile:
    write = csv.writer(csvfile)
    write.writerow(["date", "name", "state"])
    for i in range(100):
        Time = datetime.datetime.now()
        rand1 = random.randint(0, 2)
        rand2 = random.randint(0, 2)
        time.sleep(1)
        write.writerow([Time, name[rand1], state[rand2]])
end = datetime.datetime.now()
print(start, end, end-start)



