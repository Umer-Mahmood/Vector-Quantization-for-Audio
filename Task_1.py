
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import seminar_2_functions
import pickle

bit_depth = 4

#Reading audio file track48

sampling_rate, audio_signal_samples = wavfile.read('Track48.wav','r')

with open("Binary_Files\original_audio.bin","wb") as file_bin:
    pickle.dump(audio_signal_samples,file_bin)
    print("Binary file writen")

seconds_per_sample = 1/sampling_rate;

Sig_Duration= len(audio_signal_samples)*seconds_per_sample

Time=np.linspace(0, Sig_Duration, len(audio_signal_samples))


channels= seminar_2_functions.channels('Track48.wav')
# print("Playing Full original Audio")
# seminar_2_functions.signal_play(audio_signal_samples,sampling_rate,channels)


#  writing to original_audio.bin




with open("Binary_Files\original_audio.bin","rb") as file_bin:
    signal_data_from_bin = pickle.load(file_bin)
    print("Binary file Read")

encoded_signal, reconstruted_audio_data = seminar_2_functions.mid_tread(audio_signal_samples,bit_depth)

with open("Binary_Files\coded_uniform_q_signal.bin","wb") as file_bin:
    pickle.dump(encoded_signal,file_bin)
    print("mid treat encoded audio written to binary file")

with open("Binary_Files\coded_uniform_q_signal.bin","rb") as temp_bin:
    coded_signal_data_from_bin = pickle.load(temp_bin)
    print("Binary file containing encoded audio data Read")


print("Playing audio data from binarz file")
seminar_2_functions.signal_play(signal_data_from_bin,sampling_rate,channels)


fig,(a1,a2) = plt.subplots(2)
a1.plot(Time, audio_signal_samples[:,0], 'r', label='Original Signal' )
a1.plot(Time,reconstruted_audio_data[:,0], 'g:', label='Reconstructed Signal')



plt.show()



