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

def classificationLine2D(data):
    data_ = data[:,2]
    diff = np.ndarray(shape=(10000,3))
    points = []
    diff_ = np.ndarray(shape=(10000,1))
    print(len(data_))
    for i in range(9999):
        diff_[i] = data_[i+1]-data_[i]
    for i in range(9999):
        if diff_[i] >= 0.5 or diff_[i]<=-0.5:
            points.append([data[i,0],data[i,1]])
    print(max(diff_))
    print(min(diff_))
#
#        if data[i,2] is not 0:
#            print("ett")
#        else:
#            print("noll")
        
    points1 = np.ndarray(shape=(len(points),2))
    
    for i in range(len(points)):
        points1[i,0] = points[i][0]
        points1[i,1] = points[i][1]
    return points1

def main():
    a = gaussianData(2,5,[1,0],1)
    print(a[0])
    print("******")
    print(a[1])

        


    
if __name__ == '__main__':
    main()
