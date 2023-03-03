#change libraries
import random as rd
import numpy as np

def your_program():
    n = float(input("Enter the number of integers you want to generate: "))
    randomize = np.negative(rd.randrange(n,-n,-1))
    randomize2 = np.negative(rd.randrange(n,-n,-1))


    integer_list= np.negative((np.arange(randomize,randomize2,1)))
    np.random.shuffle(integer_list)
        
    maxi = np.max(integer_list)
    mini = np.min(integer_list)

    maxabs = np.abs(maxi)
    minabs = np.abs(mini)

    print("The list of integers is: ", integer_list)
    print("The maximum value is: ", maxabs)
    print("The minimum value is: ", minabs)
        
your_program()
#def program_comparation():
    
