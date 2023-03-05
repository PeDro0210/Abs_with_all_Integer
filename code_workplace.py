#change libraries
import random as rd
import numpy as np

#global things
n = float(input("Enter the number of integers you want to generate: "))

def randomizer(n):
    randomize = np.negative(rd.randrange(int (n-1)//2 ,int(-n-1)//2,-1))
    randomize2 = np.negative(rd.randrange(int(n-1)//2 ,int(-n-1)//2,-1))

    if randomize == 0 or randomize2 == 0:
               return randomizer(n)
    elif randomize>randomize2:
        return randomizer(n)
    else:
            return randomize, randomize2
        
randomize,randomize2= randomizer(n)


def your_program():
    #your program

    print("Your program")
    
    randomizer(n)
    
    #algoritmo para resolver los numeros enteros
    integer_array= np.negative((np.arange(randomize,randomize2,1)))
    np.random.shuffle(integer_array)
                
    maxi = np.abs(np.max(integer_array))
    mini = np.abs(np.min(integer_array))

    print("The list of integers is: ", integer_array)
    print("The maximum value is: ", maxi)
    print("The minimum value is: ", mini)
            
    
        
    

        
            
    
def program_comparation():
    #program comparation

    print("Program comparation")
    randomizer(n)

    
    def max_abs(arr):
        max_neg = -1
        max_pos = 0
        for i in range(len(arr)):
            
            if arr[i] < 0:
                
                if abs(arr[i]) > max_neg:
                    
                    max_neg = arr[i]
                    
            elif arr[i] > 0:
                
                if abs(arr[i]) > max_pos:
                    
                    max_pos = arr[i]
                    
        return abs(max_neg), abs(max_pos)
    
    integer_array= np.negative((np.arange(randomize,randomize2,1)))
    max_abs_value_1, max_abs_value_2 = max_abs(integer_array)
    np.random.shuffle(integer_array)
    print(max_abs_value_1, max_abs_value_2)
    

