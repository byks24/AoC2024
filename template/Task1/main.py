
result=0

if __name__ == '__main__':
    array1=[]
    array2=[]
    with open('text.txt', 'r') as f:
        for line in f: 
            print(line)
            print(line.split())
            array1.append(line.split()[0])
            array2.append(line.split()[1])
            # array = [None, None]
            # for char in range(len(line)):
            #     if line[char].isdigit():
            #         if array[0] is None:
            #             array[0] = int(line[char])
            #         else:
            #             array[1] = int(line[char])
            # if array[1] == None:
            #     array[1] = array[0]
            # result+=array[0]*10+array[1]
        array1.sort()
        array2.sort()
        for i in range(len(array1)):
            result+=abs(int(array1[i-1])-int(array2[i-1]))
        print(result)
