import os
import os.path
import math
import fileinput
import matplotlib.pyplot as plt
import random

phyrate_file = "sim6_cl0_throughputLog.txt"

data_size,data_time = [],[]
th_size, th_time = [],[]
segmentDuration = 0.1 #10*1000
segmentstart = 0
timetemp = 0
#--------------------------------------------------
with open(phyrate_file, 'r') as phyrate_to_read:
    n=0
    while True:
        lines = phyrate_to_read.readline() 
        if not lines:
            break   
        i = lines.split()
        temp_time = float(i[0])
        # print(i,temp_time,segmentstart,data_time)
        if temp_time <= segmentstart + segmentDuration:
            data_size.append(float(i[1]))
            data_time.append(float(i[0]))
        else:
            segmentstart = temp_time
            if len(data_size) == 0 or (data_time[-1]-data_time[0]) == 0:
                th_size.append(0)
                th_time.append(temp_time)
            else:
                th_size.append(sum(data_size)*8/(data_time[-1]-data_time[0]))
                th_time.append(sum(data_time)/len(data_time))
            data_size, data_time = [], []
            
        n = n+1

# print(th_size)
# print(th_time)


plt.figure(figsize=(40,24))
c = plt.subplot(111)
c1 = c.plot(th_time,th_size,'g-',label = 'sim-Throughput',linewidth=2.0)
plt.grid(True)
plt.xlabel("Time/s",fontsize=20)
plt.ylabel("Bitrate/100Mbps",fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylim(0,150000000)
plt.xlim(0,300)
handlesa,labelsa = c.get_legend_handles_labels()
c.legend(handlesa[::-1],labelsa[::-1],fontsize=20)
plt.savefig("sim-Throughput.png")
# plt.show()
