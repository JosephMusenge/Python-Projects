import random

# Given a list, find the mean, mode, and medium
list = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

# Calculate the Mean
mean = sum(list)/len(list)
print(mean)

# Calculate the Median
list.sort()
if len(list) % 2 == 0:
    m1 = list[len(list)//2] 
    m2 = list[len(list)//2 - 1]
    median = (m1 + m2) / 2
else:
    median = list[len(list)//2]
print(median)

# Calculate Mode 
frequency = {}
for i in list:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)