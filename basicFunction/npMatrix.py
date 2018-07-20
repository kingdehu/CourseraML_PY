import numpy as np
import numpy.matlib as npmatrix

class NPMatrix():
    
    def __init__(self):
        pass
    
    def getMfeature(self):
        mata = npmatrix.empty((3,4)) # random data
        mata = npmatrix.zeros((3,4)) # zeros
        mata = npmatrix.ones((3,4)) # one
        mata = npmatrix.eye(3) # one along diagonal
        mata = npmatrix.eye(3,5) # one along diagonal
        mata = npmatrix.identity(3) # identity square matrix 
        mata = npmatrix.rand(3,7) # rand data
        mata = npmatrix.ones((3,1)) # one
        print(mata)
        print(mata.shape)
        print(mata.dtype)
    
    def manipulate(self):
        mata = np.matrix([[1,2],[3,4],[5,6]])
        matb = [[1,2,3],[3,4,5],[5,6,5],[5,6,5]]
#         print(mata)
#         print(matb)
#         print(3*mata)
#         print(3+mata)
#         print(3-mata)
        print(mata)
        print(mata.transpose())
        print(mata*mata.transpose())
        print(np.multiply(mata, mata))
        
    
    
if __name__ == '__main__':
    NPM = NPMatrix()
    #NPM.getMfeature()
    NPM.manipulate()