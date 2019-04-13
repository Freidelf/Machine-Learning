import matplotlib.pyplot as plt
import kap2_kdTree2D
import GenerateData
from collections import namedtuple
from operator import itemgetter
from pprint import pformat
import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    dx = x1 - x2
    dy = y1 - y2

    return math.sqrt(dx*dx + dy*dy)

def closerDist(pivot, p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    
    d1 = distance(pivot[0:2],p1[0:2])
    d2 = distance(pivot[0:2],p2[0:2])
    
    if d1 < d2:
        return p1
    else:
        return p2
    
def oneNearestPoint(root,point,depth = 0):
    if root is None:
        return None

    axis = depth % 2

    next_branch = None
    opposite_branch = None
   
    if point[axis] < root[0][axis]:
        next_branch = root[1]
        opposite_branch = root[2]
    else:
        next_branch = root[2]
        opposite_branch = root[1]
        
    best = closerDist(point,
                          oneNearestPoint(
                              next_branch,
                              point,
                              depth + 1),
                          root[0])
    
    if distance(point[0:2], best[0:2]) > abs(point[axis] -  root[0][axis]):
        best = closerDist(point,
                              oneNearestPoint(
                                  opposite_branch,
                                  point,
                                  depth + 1),
                              best)
    return best

def pltcolor(lst):
    cols=[]
    for l in lst:
        if l==0:
            cols.append([0.53,0.81,1])
        else:
            cols.append([1,0.73,0.06])
    return cols



def main():
    obs1 = GenerateData.gaussianData(10,100,[0,1],0)[0]
    obs2 = GenerateData.gaussianData(10,100,[1,0],1)[0]
    min1 = min(min(obs1[:,0]),min(obs2[:,0]))*1.05
    max1 = max(max(obs1[:,0]),max(obs2[:,0]))*1.05
    min2 = min(min(obs1[:,1]),min(obs2[:,1]))*1.05
    max2 = max(max(obs1[:,1]),max(obs2[:,1]))*1.05
    obs11 = obs1.tolist()
    obs22 = obs2.tolist()
    X = []
    for i in range(100):
        X.append((obs1[i,0],obs1[i,1],0))
    for i in range(100):
        X.append((obs2[i,0],obs2[i,1],1))
    tree = kap2_kdTree2D.buildTree(X)
    domainRanges = [min1,max1,min2,max2]
    fillData = GenerateData.domainFillData2D(domainRanges)
    for i in range(len(fillData[:,0])):
        point = (fillData[i,0], fillData[i,1])
        t = oneNearestPoint(tree,point)
        fillData[i,2] = t[2]
    classLine = GenerateData.classificationLine2D(fillData)
#    print(classLine)
    cols=pltcolor(fillData[:,2])
    plt.plot(obs1[:,0],obs1[:,1], 'o',color=[0.53,0.81,1],fillstyle='none')
    plt.plot(obs2[:,0],obs2[:,1], 'o',color=[1,0.73,0.06],fillstyle='none')
    plt.scatter(fillData[:,0],fillData[:,1], c = cols, s = 0.3)
    plt.scatter(classLine[:,0],classLine[:,1], c =[0,0,0], s = 0.3)
    plt.xlim(min1,max1)
    plt.ylim(min2,max2)
    plt.show()
if __name__ == '__main__':
    main()
