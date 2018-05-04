no_processes = raw_input("enter number of processes")

n = int(no_processes)

arrival = [0]*n
burst = [0]*n
priority = [0]*n

for i in range(0,n):
	arrival[i] = raw_input("enter arrival time")
        burst[i] = raw_input("enter burst time")
        priority[i] = raw_input("enter priority of process")

mini = priority[0]

for i in range(0,n-1):
	for j in range(0,n-1-i):
		if arrival[j]>arrival[j+1]:
			priority[j],priority[j+1] = priority[j+1],priority[j]		       
        		arrival[j],arrival[j+1] = arrival[j+1],arrival[j]
			burst[j],burst[j+1] = burst[j+1],burst[j]

remaining = n
time = 0
time1 = 0
k = int(0)
time1 = int(burst[0])
while remaining != 0:
    if int(time) >= int(arrival[k]):
        print("time %5s    =     process %5s" % (time,k+1))
	

	if int(time) == int(time1):
		remaining = remaining - 1
                k = k+1
                time1 = time1 + int(burst[k])
		time = time + 1
		
		
		
	else:
		time = time + 1

    else:
        	time = time + 1
        	print("time %5s    =     waiting for process" % (time))
		

        
