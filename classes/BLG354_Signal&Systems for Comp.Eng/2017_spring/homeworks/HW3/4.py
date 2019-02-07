#BLG 354E 2018 May HW-3 Istanbul Technical University
#Yunus Güngör-Student No:150150701
#question 4

import numpy as np
from scipy import signal
from scipy.signal import convolve
import matplotlib.pyplot as plt

samplePerSecond = 50
frequency = 1
duration = 10
sampleNumber = np.arange(duration * samplePerSecond)
#define signal
signal =np.heaviside(sampleNumber,1)
signal = signal - np.heaviside(sampleNumber-samplePerSecond,1)

convelvedSignal = signal
for x in range(0,9):
    convelvedSignal = convolve(convelvedSignal,signal)

#change dimensions of the graph
duration = len(convelvedSignal)/samplePerSecond
sampleNumber = np.arange(duration * samplePerSecond)

#plot result
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylim([-1, 1000])
p, = ax.plot(sampleNumber / samplePerSecond, np.full(sampleNumber.shape, convelvedSignal))
p.set_data(sampleNumber / samplePerSecond, convelvedSignal)
fig.canvas.draw()
plt.show()