from pprint import pformat
import numpy as np


def gaussianData(poolSize,
                 Observations,
                 mean,
                 yVal,
                 std = 0):
    variables = len(mean)
    std = np.eye(variables)
    meanPool = np.random.multivariate_normal(mean,std,poolSize)
    ObsList = np.ndarray(shape = (Observations, variables+1))    
    for i in range(Observations):
        r = np.random.randint(0,poolSize)
        temp = np.random.multivariate_normal(
            meanPool[r],
            np.multiply(std,0.2)).tolist()
        ObsList[i,:variables] = temp
        ObsList[i,variables] = yVal
    return [ObsList, meanPool]


        
def domainFillData2D(ranges):
    outData = np.ndarray(shape = (10000,3),dtype = float)
    X1_range = ranges[1]-ranges[0]
    outData[:,0] = np.tile(ranges[0] + range(100)*X1_range/100,100)
    X2_vals = np.linspace(ranges[2],ranges[3],100)
    for i in range(100):
        outData[range(i*100,(i+1)*100),1] = np.linspace(X2_vals[i],X2_vals[i],100)
    return outData

        

def main():
    a = gaussianData(2,5,[1,0],1)
    print(a[0])
    print("******")
    print(a[1])

        

if __name__ == '__main__':
    main()
