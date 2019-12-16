import struct
import wave

import matplotlib.pyplot as plt
import numpy as np
import pyaudio
from scipy import signal
from scipy.io import wavfile


def signal_play(data, fs, channels):    #To play the audio
    p = pyaudio.PyAudio() #Initializing PYAudio
    if data.dtype == np.int8: #For 8 bit input
            #Opening the media stream
        stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=fs,
                    output=True)
        data = data.astype(np.int8).tostring()

    #Playing the media stream 
        stream.write(data)
        stream.close()
    else:
        stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=fs,
                    output=True)

        data = data.astype(np.int16).tostring()
    
        stream.write(data)
        stream.close() #Closing the media stream
   

def channels(filepath):
    data=wave.open(filepath) #Opeining WaveFile and acquiring data
    channels=wave.Wave_read.getnchannels(data) #Getting Channels
    return channels

def readFile(filepath):
    sampling_rate, audio_signal_samples = wavfile.read(filepath,'r')
    return audio_signal_samples[:,1]

def mid_tread(Signal_Data, bit_size):
    #step delta = Amax-Amin/2^N     
    step = (float(np.amax(Signal_Data))-float(np.amin(Signal_Data))) / pow (2,bit_size) 
    
    #In Mid Tread Quantizer index = round of Signal_Data/step
    index = np.round(Signal_Data/step)
    
    #Reconstruction of Signal
    reconstruct = np.array(Signal_Data.shape)

    reconstruct=index*step
    #reconstruct= reconstruct.astype(np.int8)    
    return index,reconstruct
