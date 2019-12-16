import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import seminar_2_functions
import pickle
import math
# sampling_rate, audio_signal_samples = wavfile.read('Track48.wav','r')

audio_signal_samples = seminar_2_functions.readFile('Track48.wav')


# x = [3,2,4,5]
y1 = [1,2] 
y2 = [5,6]

# audio_signal_samples_zeroth 
# x = audio_signal_samples[:,0]
# x2=x[10000+np.arange(1,100)]

halfLen = int(len(audio_signal_samples)/2)
t=np.zeros([halfLen,2])

i = 0;
h=0;

# len of x = 3
while(i < len(audio_signal_samples-1)):        # i 0 2
    t[h]=(audio_signal_samples[i],audio_signal_samples[i+1])  #    x0,x1      x2 ,x3    
    i=i+2
    h=h+1

print(t)

""" j=0
k=0
l=0

closer_to_y1 = list()
# closer_to_y1 = np.array(closer_to_y1)

closer_to_y2 = list()
# closer_to_y2 = np.array(closer_to_y1)
while(j<len(t)):
    temp = t[j]
    distance1 = math.sqrt(math.pow((temp[0]-y1[0]),2)+math.pow((temp[1]-y1[1]),2))
    distance2 = math.sqrt(math.pow((temp[0]-y2[0]),2)+math.pow((temp[1]-y2[1]),2))

    if(distance1<distance2):
    #closer = y1
        # closer_to_y1=temp
        closer_to_y1.append(temp)
        # k=k+1
    else:
    # closer = y2
        # closer_to_y1[l]=temp
        # l=l+1
        closer_to_y2.append(temp)

    j=j+1

print(closer_to_y1) """

# new y1 = average all values in closer_to_y1 
# new y2 = average all values in closer_to_y2



# print(distance1,distance2)
# trainingVector=x[np.arange(1,2)]
# print(trainingVector)