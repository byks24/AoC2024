
result=0

if __name__ == '__main__':
    d1={}
    d2={}
    with open('text.txt', 'r') as f:
        for line in f: 
            if line.split()[0] not in d1:
                d1[line.split()[0]] =1
            else:
                d1[line.split()[0]]= d1[line.split()[0]]+1
            if line.split()[1] not in d2:
                d2[line.split()[1]] =1
            else:
                d2[line.split()[1]]= d2[line.split()[1]]+1
        for key in d1:
            if key in d2:
                result+=(int(key)*int(d2[key]))*int(d1[key])
        print(result)
