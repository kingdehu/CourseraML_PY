import numpy as np
import numpy.matlib as npmatrix
import matplotlib.pyplot as plt
class LoadData:
    
    def __init__(self, path):
        self.path = path
    
    def loadTXT(self):
        rawdata = np.loadtxt(self.path, dtype=float, delimiter=',')
        X = np.c_[[1 for i in range(rawdata.shape[0])],rawdata[:,:-1]]
        X = np.matrix(X.reshape(rawdata.shape[0],rawdata.shape[1])).transpose()
        y= np.matrix(rawdata[:,-1])
        datalen = rawdata.shape[0]
        return X, y, datalen, rawdata
        
    def plot_scatter_demo(self, nb_samples=100):
        """Scatter plot.
        """
        prng = np.random.RandomState(96917002)
        for mu, sigma, marker in [(-.5, 0.75, 'o'), (0.75, 1., 's')]:
            x, y = prng.normal(loc=mu, scale=sigma, size=(2, nb_samples))
            plt.plot(x, y, ls='none', marker=marker)
        plt.show()
        
    def plotData(self,data):
        for i, marker in enumerate(['o','s']):
            plt.plot(data[np.where(data[:,2]==i)][:,0], data[np.where(data[:,2]==i)][:,1], ls='none', marker=marker)
        plt.show()
    
    
if __name__ == '__main__':
    LoadData = LoadData('.\ex2data1.txt')
    data = LoadData.loadTXT()
    #LoadData.plotData(data[0].transpose()[:,1],data[1].transpose())
    
    LoadData.plotData(data[3])
