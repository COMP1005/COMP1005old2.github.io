#
# Name : <student name>
# ID   : <student ID>
#
# heat.py - heat diffusion simulation
#
import numpy as np
import matplotlib.pyplot as plt

size = 10 

curr = np.zeros((size,size)) 
print(curr)    
for i in range(size): 
    curr[i,0] = 10 

next = np.zeros((size,size)) 

for timestep in range(5): 
    for r in range(1, size-1): 
        for c in range (1, size- 1 ): 
            next[r,c] = (curr[r-1,c-1]*0.1 + curr[r-1,c]*0.1 
                + curr[r-1,c+1]*0.1 + curr[r,c-1]*0.1 
                + curr[r,c]*0.2 + curr[r,c+1]*0.1 
                + curr[r+1,c- 1]*0.1 + curr[r+1,c]*0.1 
                + curr[r+1,c+1]*0.1) 

    for i in range(size): 
        next[i,0] = 10 

    print("Time step: ", timestep) 
    print(next)    
    curr = next.copy() 

plt.imshow(curr, cmap=plt.cm.hot) 
plt.show() 
