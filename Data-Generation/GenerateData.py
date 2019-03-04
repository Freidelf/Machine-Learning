from pprint import pformat
import numpy as np


def gaussianData(poolSize,
                 Observations,
                 mean,
                 std = 0):
    variables = len(mean)
    std = np.eye(variables)
    meanPool = np.random.multivariate_normal(mean,std,poolSize)
    ObsList = np.ndarray(shape = (Observations, variables*2))    
    for i in range(Observations):
        r = np.random.randint(0,poolSize)
        temp = meanPool[r].tolist()
        temp.extend(np.random.multivariate_normal(
            meanPool[r],
            np.multiply(std,0.2)).tolist())
        ObsList[i,:] = temp
    return ObsList

def main():
    print(gaussianData(2,5,[1,0,0,0]))

if __name__ == '__main__':
    main()
        
