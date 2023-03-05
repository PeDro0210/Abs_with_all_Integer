import numpy as np
import time as hour 
import csv as csv
from code_workplace import your_program, program_comparation
import psutil
import os

#special variables
pid = os.getpid()
start_time = hour.time()
it = int(input("how much interations you want to do: "))
nombre= input("Ingrese el nombre del archivo: ")
num= int(input("Ingrese el numero: "))

#all fix :D


#arrays 

show_time=np.zeros([it], dtype=float)
show_time2=np.zeros([it], dtype=float)





process = psutil.Process()
after_memory_usage = process.memory_info().rss

for i in range(it):
    start_time = hour.time()

    your_program(num)
    
    end_time = hour.time()
    
   

    total_time = end_time - start_time
    
    show_time[i] = total_time
    print("Iteration: ", i+1)
    print(show_time[i])

before_memory_usage = process.memory_info().rss

difference_memory_usage = max(before_memory_usage,after_memory_usage) - min(after_memory_usage,before_memory_usage)

difference_memory_usage= difference_memory_usage/it
    
print(f"the average is {difference_memory_usage}  bytes per iteration")

average_time = np.average(show_time)





process2 = psutil.Process()
after_memory_usage2 = process.memory_info().rss

for i in range (it):
    start_time2 = hour.time()
    
    program_comparation(num)
    
    end_time2 = hour.time()
    
    total_time2 = end_time2 - start_time2
    show_time2[i]=total_time2
    
    print("Iteration: ", i+1)
    print(show_time2[i])
    
before_memory_usage2 = process.memory_info().rss

difference_memory_usage2 = max(before_memory_usage2,after_memory_usage2) - min(after_memory_usage2,before_memory_usage2)

difference_memory_usage2= difference_memory_usage2/it
    
print(f"the average is {difference_memory_usage2} bytes per iteration")    

average_time2 = np.average(show_time2)






with open(f"{nombre}.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Programa 1','Programa 2'])
                writer.writerow(['Tiempo','Tiempo'])
                writer.writerow([average_time,average_time2])
                writer.writerow(['Memoria','Memoria'])
                writer.writerow([difference_memory_usage,difference_memory_usage2])
                writer.writerow(['Minimos'])
                writer.writerow([min(average_time,average_time2)])
                writer.writerow([min(difference_memory_usage,difference_memory_usage2)])
                




                
