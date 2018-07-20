import numpy as np
import numpy.matlib as npmatrix
import matplotlib.pyplot as plt
class LoadData:
    
    def __init__(self, path):
        self.path = path
    
    def loadTXT(self):
        rawdata = np.loadtxt(self.path, dtype=float, delimiter=',')
        X = np.c_[[1 for i in range(rawdata.shape[0])],rawdata[:,0]]
        X = np.matrix(X.reshape(rawdata.shape[0],2)).transpose()
        y= np.matrix(rawdata[:,1])
        datalen = rawdata.shape[0]
        return X, y, datalen
        
        
    def plotData(self, x, y):
        xx = data[0].transpose()[:,1]
        yy = -3.89 + 1.19*xx
        plt.plot(x, y, 'r+',xx,yy)
        plt.show()
    
    
if __name__ == '__main__':
    LoadData = LoadData('.\ex1data1.txt')
    data = LoadData.loadTXT()
    print(data[0])
    print(data[1])
    LoadData.plotData(data[0].transpose()[:,1],data[1].transpose())
