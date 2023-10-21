#Brittany Strong
#October 17, 2023
import queue
from collections import deque

#PROCESSES P1-P8
process = {
  1: [5, 27, 3, 31, 5, 43, 4, 18, 6, 22, 4, 26, 3, 24, 4],
  2: [4, 48, 5, 44, 7, 42, 12, 37, 9, 76, 4, 41, 9, 31, 7, 43, 8],
  3: [8, 33, 12, 41, 18, 65, 14, 21, 4, 61, 15, 18, 14, 26, 5, 31, 6],
  4: [3, 35, 4, 41, 5, 45, 3, 51, 4, 61, 5, 54, 6, 82, 5, 77, 3],
  5: [16, 24, 17, 21, 5, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4],
  6: [11, 22, 4, 8, 5, 10, 6, 12, 7, 14, 9, 18, 12, 24, 15, 30, 8],
  7: [14, 46, 17, 41, 11, 42, 15, 21, 4, 32, 7, 19, 16, 33, 10],
  8: [4, 14, 5, 33, 6, 51, 14, 73, 16, 87, 6]
}

#quantums
queue1_Tq = 5
queue2_Tq = 10


#FIRST COME FIRST SERVE SIMULATION
def fcfs_queue(process):
  #arrival queue stores arrival times for all the processes
  arrival_queue = queue.Queue()
  #wait queue will store the wait time after every process enters the scheudling
  wait_queue = queue.Queue()
  #turnaround queue will store the turnaround times of every process
  turnaround_queue = queue.Queue()

  #calculate the wait time, values from wait_time get stored in wait queue
  wait_time = 0
  #calculate the arrival time by saving the completion of last process
  arrival_time = 0
  #calaculte turnaround time, stores in turnaround queue
  turnaround_time = 0
  #total time is the final time of the final process
  total_time = 0

  #variables for function counts and averages
  average_wait = 0
  wait_count = 0
  average_turnaround = 0
  turnaround_count = 0
  average_response = 0
  response_count = 0

  for i in range(1, len(process) + 1):  # Process IDs start from 1
    arrival_queue.put(process[i][0])
    wait_queue.put(wait_time)
    turnaround_queue.put(turnaround_time)
    wait_time += process[i][0]
    turnaround_time += process[i][0] + sum(process[i][2:])  # Sum the burst times
    total_time += process[i][0] + sum(process[i][2:])
    cpu_utilization = ((total_time - wait_time )/ total_time)*90

    
  print("First Come First Serve Scheduler")
  print("Process ID\tArrival Time\tBurst Time\tWait Time\t")
  print("Arrival queue:", list(arrival_queue.queue))
  print("Wait queue:", list(wait_queue.queue))
  print("All Processes have been executed")
  print("Turnaround queue:", list(turnaround_queue.queue))
  print("Total time:", total_time)
  print("\n--------------------------------------------------")
  print("FCFS Results")
  print("CPU Utilization: ", cpu_utilization)
  
#finding the reponse timem
  while not wait_queue.empty():
    response_value = wait_queue.get()
    average_response += response_value
    response_count += 1


  # Calculate the average
  if response_count > 0:
      average_wt = average_response/ response_count
    #Average Wait time
      print("Average Response:", average_wt)
  else:
      print("The queue is empty.")



def fcfs_wait(process):
  #queues for arrivals, wait, and turnaround
  arrival_queue = queue.Queue()
  wait_queue = queue.Queue()
  turnaround_queue = queue.Queue()

  #variables to store the averages
  wait_time = 0
  arrival_time = 0
  turnaround_time = 0
  total_time = 0

  average_wait = 0
  wait_count = 0
  average_turnaround = 0
  turnaround_count = 0
  average_response = 0
  response_count = 0


  for i in range(1, len(process) + 1):  # Process IDs start from 1
    arrival_queue.put(process[i][0])
    wait_queue.put(wait_time)
    turnaround_queue.put(turnaround_time)
    wait_time += process[i][0]
    turnaround_time += process[i][0] + sum(process[i][2:])  # Sum the burst times
    total_time += process[i][0] + sum(process[i][2:])
    cpu_utilization = ((total_time - wait_time) / total_time)*100


  #finding the reponse timem
  while not wait_queue.empty():
    wait_value = wait_queue.get()
    average_wait += wait_value
    wait_count += 1
  #Average Wait Time
  print("All Processes have been executed")
  print("Average Wait Time:",(average_wait+total_time)/14)



def fcfs_turnaround(process):
  #arrival, wait, turnaround queues
  arrival_queue = queue.Queue()
  wait_queue = queue.Queue()
  turnaround_queue = queue.Queue()

  wait_time = 0
  arrival_time = 0
  turnaround_time = 0
  total_time = 0

  average_wait = 0
  wait_count = 0
  average_turnaround = 0
  turnaround_count = 0
  average_response = 0
  response_count = 0


  for i in range(1, len(process) + 1):  # Process IDs start from 1
    arrival_queue.put(process[i][0])
    wait_queue.put(wait_time)
    turnaround_queue.put(turnaround_time)
    wait_time += process[i][0]
    turnaround_time += process[i][0] + sum(process[i][2:])  # Sum the burst times
    total_time += process[i][0] + sum(process[i][2:])
    cpu_utilization = ((total_time - wait_time) / total_time)*100
    
  while not turnaround_queue.empty():
    #turnaround = completion time - arrival time
    #turnaround = burst times sum + wait time
    turnaround_value = turnaround_queue.get()
    average_turnaround += turnaround_value
    turnaround_count += 1
  print("Average Turnaround:", (average_turnaround/turnaround_count)/2)
  print("\n---------------------------------------------------")
  #print("Average Turnaround",(average_turnaround*turnaround_count)


#SHORTEST JOB FIRST SIMULATION
def SJF_queue(process):
  arrival_time = 0
  arrival_queue = queue.Queue()
  turnaround_queue = queue.Queue()
  turnaround_time = 0
  total_time = 0
  process_queue = queue.Queue()
  process_queue.put(arrival_time)
  
  wait_time = 0
  wait_count = 0
  average_wait = 0
  wait_queue = queue.Queue()

  for i in range(1, len(process) + 1):  # Process IDs start from 1
    arrival_queue.put(process[i][1])
    wait_queue.put(wait_time)
    turnaround_queue.put(turnaround_time)
    wait_time += process[i][1]
    turnaround_time += process[i][1] + sum(process[i][2:])  # Sum the burst times
    total_time += process[i][1] + sum(process[i][4:])
    cpu_utilization = ((total_time - wait_time) / total_time)*100

  print("\nShortest Job First Scheduler")
  #print("CPU Utilization: ",cpu_utilization)
  print("Arrival queue:", list(arrival_queue.queue))
  #print("Wait queue:", list(wait_queue.queue))
  print("Turnaround queue:", list(turnaround_queue.queue))
  print("Total time:", total_time)
  
  for p in range(1, len(process) + 1):
    if p+2 < p+4:
      process_queue.put(p+2)
      process_queue.put(p+3)
    else:
      process_queue.put(p+4)
      process_queue.put(p+5)

  while not process_queue.empty():
    process_value = process_queue.get()
    wait_time += process_value
    wait_count +=1
    wait_queue.put(wait_time)
    average_wait = (wait_time/wait_count)*10

    
 # print("\nProcess Queue:", process_queue.queue)
  print(f"Wait Queue: {wait_queue.queue}")
  print(f"Wait Time: {wait_time}")

  print("\n--------------------------------------------")
  print("SJF Results")
  print("CPU Utilization: ",cpu_utilization)
  print(f"Average Wait Time: {average_wait}")
  
    

def SFJ_turnaround(prcocess):
  arrival_time = 0
  process_queue = queue.Queue()
  process_queue.put(arrival_time)
  
  wait_time = 0
  wait_count = 0
  average_wait = 0
  wait_queue = queue.Queue()

  turnaround_time = 0
  turnaround_count = 0
  average_turnaround = 0
  turnaround_queue = queue.Queue()


  for p in range(1, len(process) + 1):
    if p+2 < p+4:
      process_queue.put(p+2)
      process_queue.put(p+3)
    else:
      process_queue.put(p+4)
      process_queue.put(p+5)
      
  while not process_queue.empty():
    process_value = process_queue.get()
    wait_time += process_value
    turnaround_time += process_value + wait_time
    wait_count +=1
    wait_queue.put(wait_time)
    turnaround_count += 1
    turnaround_queue.put(turnaround_time)
    
    average_turnaround = (turnaround_time/turnaround_count)*10
  print(f"Average Turnaround: {average_turnaround}")
    
    

def SJF_Response(process):
  #arrival, wait, and turnaround variables, queues
  arrival_time = 0
  arrival_queue = queue.Queue()
  turnaround_queue = queue.Queue()
  turnaround_time = 0
  total_time = 0
  process_queue = queue.Queue()
  process_queue.put(arrival_time)

  wait_time = 0
  wait_count = 0
  average_wait = 0
  average_response = 0
  response_count = 0
  wait_queue = queue.Queue()

  for p in range(1, len(process) + 1):
    if p+2 < p+4:
      process_queue.put(p+2)
      process_queue.put(p+3)
    else:
      process_queue.put(p+4)
      process_queue.put(p+5)

  while not process_queue.empty():
    response_value = process_queue.get()
    average_response += response_value
    response_count += 1


    # Calculate the average
  if response_count > 0:
    average_wt = average_response/ response_count
      #Average Wait time
    print("Average Response:", average_wt)
  else:
    print("The queue is empty.")
   

#Begin Multilevel Feedback Queue
#Round Robin Start
def execute_mlfq(processes, queue1_Tq, queue2_Tq):
    # Create queues for each priority level
  queues = [deque() for _ in range(3)]
  
  # Initialize the queues with the processes in Queue 1
  queues[0].extend(processes[1])

  time = 0
  while any(queues):
      for i, queue in enumerate(queues):
          if not queue:
              continue
          process = queue.popleft()
          time_quantum = queue1_Tq if i == 0 else queue2_Tq
          if process <= time_quantum:
              # Process completes within its time quantum
              time += process
              print("--------------------------------------------")
              print("\nMultilevel Feedback Queue:")
              print(f"Process {i+1} executed for {process} units at time {time}")
          else:
              # Process does not complete within its time quantum
              time += time_quantum
              print(f"Process {i+1} executed for {time_quantum} units at time {time}")
              if i < len(queues) - 1:
                  # Check if there is a next lower-priority queue
                  queues[i + 1].append(process - time_quantum)

  
  print("All processes have been executed.")
  # Create queues for each priority level
  queues = [deque() for _ in range(3)]

  # Initialize the queues with the processes in Queue 1
  queues[0].extend(processes[1])

  time = 0
  wait_times = [0] * len(queues)
  turnaround_times = [0] * len(queues)
  total_burst_time = sum(sum(queue) for queue in processes.values())

  while any(queues):
      for i, queue in enumerate(queues):
          if not queue:
              continue
          process = queue.popleft()
          time_quantum = queue1_Tq if i == 0 else queue2_Tq
          if process <= time_quantum:
              # Process completes within its time quantum
              time += process
              wait_times[i] += time
              turnaround_times[i] += time
              print(f"Process {i+1} executed for {process} units at time {time}")
          else:
              # Process does not complete within its time quantum
              time += time_quantum
              wait_times[i] += time_quantum
              print(f"Process {i+1} executed for {time_quantum} units at time {time}")
              if i < len(queues) - 1:
                  # Check if there is a next lower-priority queue
                  queues[i + 1].append(process - time_quantum)

  print("All processes have been executed.")

  # Calculate CPU utilization
  cpu_utilization = (total_burst_time - sum(wait_times)) / total_burst_time * 200

  # Print wait times, turnaround times, and CPU utilization
  for i, wait_time in enumerate(wait_times):
      turnaround_times[i] += wait_time
      print(f"Queue {i + 1} Wait Time: {wait_time}")
      print(f"Queue {i + 1} Turnaround Time: {turnaround_times[i]}")
  print(f"CPU Utilization: {cpu_utilization}%")

def mlfq_wait(process):
  arrival_queue = queue.Queue()
  wait_queue = queue.Queue()
  turnaround_queue = queue.Queue()

  wait_time = 0
  arrival_time = 0
  turnaround_time = 0
  total_time = 0

  average_wait = 0
  wait_count = 0
  average_turnaround = 0
  turnaround_count = 0
  average_response = 0
  response_count = 0


  for i in range(1, len(process) + 1):  # Process IDs start from 1
    arrival_queue.put(process[i][0])
    wait_queue.put(wait_time)
    turnaround_queue.put(turnaround_time)
    wait_time += process[i][0]
    turnaround_time += process[i][0] + sum(process[i][2:])  # Sum the burst times
    total_time += process[i][0] + sum(process[i][2:])
    cpu_utilization = ((total_time - wait_time) / total_time)*100


  #finding the reponse timem
  while not wait_queue.empty():
    wait_value = wait_queue.get()
    average_wait += wait_value
    wait_count += 1
  #Average Wait Time
  print("All Processes have been executed")
  print("Average Wait Time:",(average_wait+total_time)/14)


def mlfq_turnaround(process):
  arrival_time = 0
  process_queue = queue.Queue()
  process_queue.put(arrival_time)

  wait_time = 0
  wait_count = 0
  average_wait = 0
  wait_queue = queue.Queue()

  turnaround_time = 0
  turnaround_count = 0
  average_turnaround = 0
  turnaround_queue = queue.Queue()


  for p in range(1, len(process) + 1):
    if p+2 < p+4:
      process_queue.put(p+2)
      process_queue.put(p+3)
    else:
      process_queue.put(p+4)
      process_queue.put(p+5)

  while not process_queue.empty():
    process_value = process_queue.get()
    wait_time += process_value
    turnaround_time += process_value + wait_time
    wait_count +=1
    wait_queue.put(wait_time)
    turnaround_count += 1
    turnaround_queue.put(turnaround_time)

    average_turnaround = (turnaround_time/turnaround_count)*10
  print(f"Average Turnaround: {average_turnaround}")


def mlfq_response(process):
   #arrival queue stores arrival times for all the processes
    arrival_queue = queue.Queue()
    #wait queue will store the wait time after every process enters the scheudling
    wait_queue = queue.Queue()
    #turnaround queue will store the turnaround times of every process
    turnaround_queue = queue.Queue()

    #calculate the wait time, values from wait_time get stored in wait queue
    wait_time = 0
    #calculate the arrival time by saving the completion of last process
    arrival_time = 0
    #calaculte turnaround time, stores in turnaround queue
    turnaround_time = 0
    #total time is the final time of the final process
    total_time = 0

    #variables for function counts and averages
    average_wait = 0
    wait_count = 0
    average_turnaround = 0
    turnaround_count = 0
    average_response = 0
    response_count = 0

    for i in range(1, len(process) + 1):  # Process IDs start from 1
      arrival_queue.put(process[i][0])
      wait_queue.put(wait_time)
      turnaround_queue.put(turnaround_time)
      wait_time += process[i][0]
      turnaround_time += process[i][0] + sum(process[i][2:])  # Sum the burst times
      total_time += process[i][0] + sum(process[i][2:])
      cpu_utilization = ((total_time - wait_time )/ total_time)*90

    print("\n--------------------------------------------------")
    print("Multilevel Feedback QueueScheduler")
    print("Process ID\tArrival Time\tBurst Time\tWait Time\t")
    print("Arrival queue:", list(arrival_queue.queue))
    print("Wait queue:", list(wait_queue.queue))
    print("All Processes have been executed")
    print("Turnaround queue:", list(turnaround_queue.queue))
    print("Total time:", total_time)
   
    

  #finding the reponse timem
    while not wait_queue.empty():
      response_value = wait_queue.get()
      average_response += response_value
      response_count += 1


    # Calculate the average
    if response_count > 0:
        average_wt = average_response/ response_count
      #Average Wait time
        print("Average Response:", average_wt)
    else:
        print("The queue is empty.")



#Calling all the process functions
fcfs_queue(process)

fcfs_wait(process)

fcfs_turnaround(process)

SJF_queue(process)

SFJ_turnaround(process)

SJF_Response(process)

execute_mlfq(process, queue1_Tq, queue2_Tq)

mlfq_wait(process)

mlfq_turnaround(process)

mlfq_response(process)


