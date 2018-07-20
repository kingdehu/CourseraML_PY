import numpy as np
from LoadData import LoadData
import matplotlib.pyplot as plt

class GradientDescent():
    
    #def __init__(self, X, y, theta, alpha, batch_size):
    def __init__(self):
        
        self.rawdata = LoadData('.\ex2data1.txt')
        self.X, self.y, self.batch_size, rawdata = self.rawdata.loadTXT()
        self.theta = np.array([[0.],[0.],[0.]])
        self.alpha = 0.01
        self.costlst = []
        self.thetalst = []
        self.rawdata_p = rawdata[np.where(rawdata[:,2]==1)]
        self.rawdata_n = rawdata[np.where(rawdata[:,2]==0)]
#         print(self.theta.shape)
#         print(self.batch_size)
#         print(self.rawdata_p)
#         print(self.rawdata_n)
        self.y = self.y[0]

    
    def sigmoid(self,inputs):
        inputs = np.array(inputs)
        sigmoid_scores = [1/float(1 + np.exp(-x)) for x in inputs[0]]
        return sigmoid_scores
        
    def costFunction(self):
        h = np.matrix(self.sigmoid(self.theta.transpose()*self.X))
        print(-self.y.transpose()*np.log(h))
        print((1-self.y.transpose())*np.log(1-h))
        return 1/(self.batch_size) * np.sum(-self.y.transpose()*np.log(h) - (1-self.y.transpose())*np.log(1-h))
        
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
    for i in range(50):
        GD.gradientDescent()
    GD.plotCostJ()
