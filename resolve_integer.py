#change libraries
import random as rd
import numpy as np

def your_program():
    # Write your code here
    randomize = rd.randrange(100,-100,-1)
    randomize2 = rd.randrange(100,-100,-1)

    integer_list= np.negative([randomize,randomize2])

    maxi = np.max(integer_list)
    mini = np.min(integer_list)

    maxabs = np.abs(maxi)
    minabs = np.abs(mini)


    print("The maximum value is: ", maxabs)
    print("The minimum value is: ", minabs)
    
    
def program_comparation():
    #write the other program here
    randomize = rd.randint(-100, 100)
    randomize2 = rd.randint(-100, 100)


    integer_list = np.array([-randomize, -randomize2])

    maxabs = np.max(np.abs(integer_list))
    minabs = np.min(np.abs(integer_list))

    print("The maximum absolute value is:", maxabs)
    print("The minimum absolute value is:", minabs)
    
