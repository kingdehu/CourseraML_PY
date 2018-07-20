import numpy as np
import matplotlib.pyplot as plt

def sigmoid(inputs):
    sigmoid_scores = [1/float(1 + np.exp(-x)) for x in inputs]
    return sigmoid_scores

def plot(x,y):
    plt.plot(x, y, 'r--')
    plt.show()
    
t = np.arange(-10., 10.1, 0.1)
print(t)
print(np.sum(t))
print(sigmoid(t))
print(np.sum(sigmoid(t)))

plot(t,sigmoid(t))


