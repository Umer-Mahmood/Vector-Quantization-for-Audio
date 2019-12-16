import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import seminar_2_functions
import pickle
import math

x = [3,2,4,5,7,8,8,9,11,12,25,26]
y1 = [1,2] 
y2 = [5,6]

t={}
i = 0;
while(i < len(x)):        # i 4
    t[i] = [x[i],x[i+1]]    #    x0,x1      x2 ,x3   
    i=i+2


print(t)
print(t[0])
j=0

closer_to_y1 = {}
closer_to_y2 = {}

print(type(closer_to_y1))


k=0
l=0
while(j<len(t)):
    temp = t[j]
    distance1 = math.sqrt(math.pow((temp[0]-y1[0]),2)+math.pow((temp[1]-y1[1]),2))
    distance2 = math.sqrt(math.pow((temp[0]-y2[0]),2)+math.pow((temp[1]-y2[1]),2))

    # if(distance1<distance2):
    # #closer = y1
    #     closer_to_y1[k]=temp
    #     k=k+1
    # else:
    # # closer = y2
    #     closer_to_y1[l]=temp
    #     l=l+1

    j=j+1



# new y1 = average all values in closer_to_y1 
# new y2 = average all values in closer_to_y2
print(closer_to_y1)

print(closer_to_y2)



# print(distance1,distance2)
# trainingVector=x[np.arange(1,2)]
# print(trainingVector)