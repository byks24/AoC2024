
result=0

if __name__ == '__main__':
    d1={}
    d2={}
    with open('text.txt', 'r') as f:
        for line in f: 
            print(line)
            print(line.split())
            if line.split()[0] not in d1:
                d1[line.split()[0]] =1
            else:
                d1[line.split()[0]]= d1[line.split()[0]]+1
            if line.split()[1] not in d2:
                d2[line.split()[1]] =1
            else:
                d2[line.split()[1]]= d2[line.split()[1]]+1

            
            print(d1)
            print(d2)
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
        #for i in range(len(d1)):
            #result+=abs(int(d1[i-1])-int(d2[i-1]))
        for key in d1:
            
            print(key)
            if key in d2:
                print(d2[key])
                print("esult")
                print(int(key)*int(d2[key]))
                result+=(int(key)*int(d2[key]))*int(d1[key])
            else:
                print("not in")
                print(key)
            print("-----")
            #if line.split()[0] not in d1:

        print(result)
