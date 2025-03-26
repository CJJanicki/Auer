import sounddevice as sd
import numpy as np


fs = 48000
duration = 5
myarray = np.zeros((int(fs*duration),1))

myrecording = sd.rec(int(fs*duration),channels=1)
sd.wait()
sd.play(myrecording, fs)
sd.wait()
