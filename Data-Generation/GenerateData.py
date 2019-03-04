from pprint import pformat
import numpy as np


def gaussianData(poolSize,
                 Observations,
                 mean,
                 std = 0):
    variables = len(mean)
    std = np.eye(variables)
    meanPool = np.random.multivariate_normal(mean,std,poolSize)
    print(meanPool)
    ObsList = [[0]*variables] * Observations
    for i in range(Observations):
        if poolSize > 1:
            r = np.random.randint(0,poolSize)
        else:
            r = 0
        ObsList[i] = (np.random.multivariate_normal(
            meanPool[r],
            np.multiply(std,0.2)),
                      meanPool[r])
    return ObsList

def main():
    print(gaussianData(3,10,[1,0]))

if __name__ == '__main__':
    main()
        
