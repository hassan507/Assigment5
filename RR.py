no_processes = raw_input("enter number of processes")

timeslice = raw_input("enter time slice")
m = int(timeslice)
n = int(no_processes)

arrival = [0]*n
burst = [0]*n
number = [0]*n
ready = [0]*n

for i in range(0,n):
        number[i] = raw_input("enter number of process")
	arrival[i] = raw_input("enter arrival time")
        burst[i] = raw_input("enter burst time")
        


for i in range(0,n-1):
	for j in range(0,n-1-i):
		if arrival[j]>arrival[j+1]:
			number[j],number[j+1] = number[j+1],number[j]		       
        		arrival[j],arrival[j+1] = arrival[j+1],arrival[j]
			burst[j],burst[j+1] = burst[j+1],burst[j]

remaining = n
time = 0
time1 = 0

k = int(0)
i = int(0)
j = int(0)

while remaining != 0:
	
	y = int(ready[i]-1)
	
	if int(ready[0])==0:
		time = time + 1;
		if int(time)==int(arrival[k]):
			ready[i] = int(number[k])
		else:
			print("time %5s    =     waiting for process" % (time))
	elif int(time)>=int(arrival[y]):
		for x in range(0,m):
			print("time %5s    =     process%5s" % (time,number[y]))
			time = time + 1
			burst[y] = int(burst[y]) - 1
		p = int(time)-int(timeslice)
		if int(arrival[y+1])>=int(p) and int(arrival[y+1])<int(time):
			j = j + 1
			ready[j] = int(number[y+1])
		if int(burst[y])>0:
			j = j + 1
			ready[j] = int(number[y])
			
		else:
			remaining = remaining - 1
		i = i + 1	
