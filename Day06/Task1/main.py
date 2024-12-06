
result=0
direction=0#0top 1bot 2left 3right
dc=0
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
if __name__ == '__main__':
    array1=np.zeros((0,0))
    with open('text.txt', 'r') as f:
        for line in f: 
            size=(len(line.rstrip()))
            for char in range(len(line.rstrip())):
                array1=np.append(array1, line[char])
    array1=np.reshape(array1,(-1,size))
    unique, counts = np.unique(array1, return_counts=True)
    turns=dict(zip(unique, counts))['#']
    print(turns)
    if any('^' in xx for xx in array1):
        y=np.where(array1 == "^")[0][0]
        x=np.where(array1[y] == "^")[0][0]
        direction=0
    if any('v' in x for x in array1):
        y=np.where(array1 == "v")[0][0]
        x=np.where(array1[y] == "v")[0][0]
        direction=1
    if any('>' in x for x in array1):
        y=np.where(array1 == ">")[0][0]
        x=np.where(array1[y] == ">")[0][0]
        direction=3
    if any('<' in x for x in array1):
        y=np.where(array1 == "<")[0][0]
        x=np.where(array1[y] == "<")[0][0]
        direction=2
    while dc<=turns+2:

        if direction==0:

            for i in range(y+1):
                if y-i-1<0:
                    array1[y-i][x]="@"
                    dc+=1
                    break
                elif array1[y-i-1][x]!="#":
                    array1[y-i][x]="@"
                else:
                    dc+=1
                    direction=3
                    array1[y-i][x]=">"
                    y=y-i
                    x=x
                    break
        if direction==1:

            for i in range(array1.shape[0]-y):
                if y+i+1==array1.shape[0]:
                    array1[y+i][x]="@"
                    dc+=1
                    break
                elif array1[y+i+1][x]!="#":

                    array1[y+i][x]="@"

                else:
                    dc+=1
                    direction=2
                    array1[y+i][x]="<"
                    y=y+i
                    x=x
                    break
        if direction==2:

            
            for i in range(x+1):
                if x-i-1<0:
                    array1[y][x-i]="@"
                    dc+=1
                    break
                if array1[y][x-i-1]!="#":

                    array1[y][x-i]="@"
                else:
                    dc+=1
                    direction=0
                    array1[y][x-i]="^"
                    y=y
                    x=x-i
                    break
        if direction==3:

            for i in range(array1.shape[1]-x):            
                if x+i+1==array1.shape[1]:
                    array1[y][x+i]="@"
                    dc+=1
                    break
                if array1[y][x+i+1]!="#" and not x+i+1>array1.shape[1]:

                    array1[y][x+i]="@"
                else:
                    dc+=1
                    direction=1
                    array1[y][x+i]="v"
                    y=y
                    x=x+i
                    break
    
    print(array1)                
    unique2, counts2 = np.unique(array1, return_counts=True)
    print(dict(zip(unique2, counts2))['@'])