import random as r
import numpy as np

iat = []
st = []
arrival_time = []
service_start = []
service_End = []
waiting_time = []

queue_list = []
queue = 0
queue_list_data = []
idletime = 0
print("Customer \t IAT \t ST \t Arrival Time \t Service Start \t Service End \t Waiting Time \t Queue \t")


for i in range(10):
    iat.append(r.randint(1, 7))
    st.append(r.randint(4, 8))

    if i == 0:
        arrival_time.append(iat[i])
        service_start.append(iat[i])
        waiting_time.append(service_start[i]-arrival_time[i])
        service_End.append(service_start[i]+st[i])
        queue_list.append(service_End[i])
        queue = len(queue_list)-1
        queue_list_data.append(queue)
        idletime += service_start[i]
    else:
        arrival_time.append(arrival_time[i-1]+iat[i])

        if arrival_time[i] < service_End[i-1]:
            service_start.append(service_End[i-1])
        else:
            service_start.append(arrival_time[i])
        service_End.append(service_start[i]+st[i])
        idletime += service_start[i]-service_End[i-1]
        waiting_time.append(service_start[i]-arrival_time[i])
        if(len(queue_list) > 0):

            if(arrival_time[i] < queue_list[0]):
                queue_list.append(service_End[i])
                queue = len(queue_list)-1
                queue_list_data.append(queue)
                

            else:
                while(len(queue_list) > 0):
                    if(arrival_time[i] >= queue_list[0]):
                        queue_list.pop(0)
                    else:
                        break
                queue_list.append(service_End[i])
                queue = len(queue_list)-1
                queue_list_data.append(queue)
                    
            # if(len(queue_list) > 0):
            #     queue = len(queue_list)-1
            #     queue_list_data.append(queue)
        else:
            queue_list.append(0)

    print(f"{i+1} \t\t {iat[i]} \t {st[i]} \t\t {arrival_time[i]} \t\t {service_start[i]} \t\t {service_End[i]} \t\t {waiting_time[i]} \t {queue}\t\t")


avg_waiting_time = np.mean(waiting_time)
max_queue_length = max(queue_list_data)
server_idle_time = idletime/service_End[-1]

print(f"Average Waiting Time: {round(avg_waiting_time,2)} minutes")
print(f"Maximum Queue Length: {max_queue_length} customers")
print(f"Server Idle Time: {round(server_idle_time,3)*100} %")
