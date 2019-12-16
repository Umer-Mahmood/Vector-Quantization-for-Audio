import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import seminar_2_functions
import pickle


bit_depth = 4

sampling_rate, audio_signal_samples = wavfile.read('Track48.wav','r')

print("Reading wav file compeleted")

encoded_signal, reconstruted_audio_data = seminar_2_functions.mid_tread(audio_signal_samples,bit_depth)

print("signal quantization and reconstruction completed")

seconds_per_sample = 1/sampling_rate;

Sig_Duration= len(audio_signal_samples)*seconds_per_sample

Time=np.linspace(0, Sig_Duration, len(audio_signal_samples))

with open("Binary_Files\coded_uniform_q_signal.bin","wb") as file_bin:
    pickle.dump(encoded_signal,file_bin)
    print("mid treat encoded audio data written to binary file")

fig,(a1,a2) = plt.subplots(2)
a1.plot(Time, audio_signal_samples[:,0], 'r', label='Original Signal' )
a1.plot(Time,reconstruted_audio_data[:,0], 'g:', label='Reconstructed Signal')
plt.show()