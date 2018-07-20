import numpy as np
from LoadData import LoadData
import matplotlib.pyplot as plt

class GradientDescent():
    
    #def __init__(self, X, y, theta, alpha, batch_size):
    def __init__(self):
        
        self.rawdata = LoadData('.\ex1data1.txt')
        self.X, self.y, self.batch_size = self.rawdata.loadTXT()
        self.theta = np.array([[0.],[0.]])
        self.alpha = 0.01
        self.costlst = []
        self.thetalst = []
        
        print(self.theta.shape)
        print(self.batch_size)
        print(np.sum(self.X[:,1]))
        print(np.sum(self.y))
        
    def costFunction(self):
        
        return 1/(2*self.batch_size) * np.sum(np.square(self.theta.transpose()*self.X-self.y))
        
    def gradientDescent(self):
        
        diff = self.theta.transpose()*self.X - self.y
        self.theta -= self.alpha*(1/self.batch_size) * self.X*diff.transpose()  
        self.thetalst.append(self.theta)  
        self.costlst.append(self.costFunction())
    
    def plotCostJ(self):
        x = [i for i in range(len(self.costlst))]
        plt.plot(x, self.costlst)
        
    def plotCostJTheta(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        x = self.thetalst[0]
        y = self.thetalst[1]
        z = self.costlst
        ax.plot(x, y, z, label='parametric curve')
        ax.legend()
        plt.show()
    
if __name__ == '__main__':
    GD = GradientDescent()
    for i in range(5000):
        GD.gradientDescent()
    GD.plotCostJ()
