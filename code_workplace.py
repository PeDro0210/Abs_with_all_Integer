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
                
    maxi = np.max(integer_array)
    mini = np.min(integer_array)

    maxabs = np.abs(maxi)
    minabs = np.abs(mini)

    print("The list of integers is: ", integer_array)
    print("The maximum value is: ", maxabs)
    print("The minimum value is: ", minabs)
            
    
        
    

        
            
    
def program_comparation():
    #program comparation
    print("Program comparation")
    randomizer(n)

    
    def max_abs(arr):
        max_val = None
        for i in range(len(arr)):
            if max_val is None or abs(arr[i]) > abs(max_val):
                max_val = arr[i]
        return abs(max_val)

# Example usage:
    integer_array= np.negative((np.arange(randomize,randomize2,1)))
    max_abs_value = max_abs(integer_array)
    print(max_abs_value)



    
