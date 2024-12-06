
result=0
direction=0#0top 1bot 2left 3right
dc=0
end=0
points=0
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
    #print(turns)


    for yyy in range(array1.shape[0]):
        for xxx in range(array1.shape[1]):
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
            startx=x
            starty=y
            if(xxx==startx and yyy==starty):
                continue
            print("newarr")
            arraycp=np.copy(array1)
            
            arraycp[yyy][xxx]="#"
            end=0
            dc=0
            while end==0 and dc<=2*turns+2:
                print(yyy)
                if direction==0:

                    for i in range(y+1):
                        if y-i-1<0:
                            arraycp[y-i][x]="@"
                            end=1
                            break
                        elif arraycp[y-i-1][x]!="#":
                            arraycp[y-i][x]="@"
                        else:
                            dc+=1
                            direction=3
                            arraycp[y-i][x]=">"
                            y=y-i
                            x=x
                            break
                        #print(arraycp)
                if direction==1:

                    for i in range(arraycp.shape[0]-y+1):
                        if y+i+1==arraycp.shape[0]:
                            arraycp[y+i][x]="@"
                            end=1
                            break
                        elif arraycp[y+i+1][x]!="#":

                            arraycp[y+i][x]="@"

                        else:
                            dc+=1
                            direction=2
                            arraycp[y+i][x]="<"
                            y=y+i
                            x=x
                            break
                if direction==2:

                    
                    for i in range(x+1):
                        if x-i-1<0:
                            arraycp[y][x-i]="@"
                            end=1
                            break
                        if arraycp[y][x-i-1]!="#":

                            arraycp[y][x-i]="@"
                        else:
                            dc+=1
                            direction=0
                            arraycp[y][x-i]="^"
                            y=y
                            x=x-i
                            break
                if direction==3:

                    for i in range(arraycp.shape[1]-x+1):            
                        if x+i+1==arraycp.shape[1]:
                            arraycp[y][x+i]="@"
                            end=1
                            break
                        if arraycp[y][x+i+1]!="#" and not x+i+1>arraycp.shape[1]:

                            arraycp[y][x+i]="@"
                        else:
                            dc+=1
                            direction=1
                            arraycp[y][x+i]="v"
                            y=y
                            x=x+i
                            break
                #print(yyy,xxx)
                #print(arraycp)
            if end==0:
                points+=1
                #print(yyy,xxx)
                #print(arraycp)                
    #unique2, counts2 = np.unique(array1, return_counts=True)
   # print(dict(zip(unique2, counts2))['@'])
    print(points)