import numpy as np
import time as hour 
import csv as csv
from code_workplace import your_program, program_comparation

start_time = hour.time()
nombre= input("Ingrese el nombre del archivo: ")

n=100
show_time=np.zeros([n])
show_time2=np.zeros([n])



for i in range (n):

    your_program()
    
    end_time = hour.time()

    total_time = end_time - start_time
    
    show_time[i]=total_time
    
    print(total_time)

average_time = np.sum(show_time)/n

for i in range (n):
    
    program_comparation()
    
    end_time2 = hour.time()

    total_time2 = end_time2 - start_time

    show_time2[i]=total_time2
    
    
    print(total_time2)

average_time2 = np.sum(show_time2)/n

with open(f"{nombre}.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['el mio','el de chatgpt'])
                writer.writerow([total_time,total_time2])
                writer.writerow(['promedio','promedio'])
                writer.writerow([average_time,average_time2])



                
