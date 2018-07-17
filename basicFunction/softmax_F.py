#calculates the probabilities distribution of the event over n different events

import numpy as np
import matplotlib.pyplot as plt

def softmax(inputs):
    softmax_scores = [np.exp(x)/np.sum(float(np.exp(inputs))) for x in inputs]
    return softmax_scores

def plot(x,y):
    plt.plot(x, y, 'r--')
    plt.show()
    
t = np.arange(-1000., 1000., 100)
print t
print softmax(t)
print np.sum(softmax(t))
plot(t,softmax(t))
