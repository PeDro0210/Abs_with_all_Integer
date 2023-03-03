import numpy as np
import time as hour 
import csv as csv
from code_workplace import your_program, program_comparation

start_time = hour.time()
nombre= input("Ingrese el nombre del archivo: ")

n=100
show_time=np.zeros([n], dtype=float)
show_time2=np.zeros([n], dtype=float)

#por si hay cambios

for i in range (n):
    start_time = hour.time()
    
    your_program()
    
    end_time = hour.time()
    
    float;
    total_time = end_time - start_time
    show_time[i]=total_time
    
    print(show_time[i])
average_time = np.average(show_time)

for i in range (n):
    start_time2 = hour.time()
    
    program_comparation()
    
    end_time2 = hour.time()
    
    float;
    total_time2 = end_time2 - start_time2
    show_time2[i]=total_time2
    
    
    print(show_time2[i])
average_time2 = np.average(show_time2)

if average_time>average_time2:
    with open(f"{nombre}.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['el mio','el de chatgpt'])
                writer.writerow([average_time,average_time2])
                writer.writerow(['Program 2 gana'])
                writer.writerow([min(average_time,average_time2)])

else:
    with open(f"{nombre}.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['el mio','el de chatgpt'])
                writer.writerow([average_time,average_time2])
                writer.writerow(['Program 1 gana'])
                writer.writerow([min(average_time,average_time2)])



                
