
result=0

if __name__ == '__main__':
    array1=[]
    array2=[]
    with open('text.txt', 'r') as f:
        for line in f: 
            array1.append(line.split()[0])
            array2.append(line.split()[1])
        for i in range(len(array1)):
            result+=abs(int(array1[i-1])-int(array2[i-1]))
        print(result)
