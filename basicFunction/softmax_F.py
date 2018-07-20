#calculates the probabilities distribution of the event over n different events

import numpy as np
import matplotlib.pyplot as plt

def softmax(inputs):
    softmax_scores = [np.exp(x)/float(np.sum(np.exp(inputs))) for x in inputs]
    return softmax_scores

def plot(x,y):
    plt.plot(x, y, 'r--')
    plt.show()
    
t = np.arange(-10., 10., 0.1)
print(t)
print(softmax(t))
print(np.sum(softmax(t)))
plot(t,softmax(t))
