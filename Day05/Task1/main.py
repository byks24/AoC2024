
result=0

if __name__ == '__main__':
    d1={}
    with open('text.txt', 'r') as f:
        for line in f: 

            if line.split("|")[0] in d1:
                d1[line.split("|")[0]] += "," +line.split("|")[1].rstrip() 
            else:
                d1[line.split("|")[0]] = line.split("|")[1].rstrip()
        print(d1)
    with open('tex2.txt', 'r') as f2:
        for line2 in f2: 
            prev=[]
            counter=0
            stop=0
            for i in line2.split(","):
                prev.append(i.rstrip())
                if counter==0:
                    for j in prev:
                        if i.rstrip() in d1:
                            if i.rstrip() in d1 and j in d1[i.rstrip()].split(","):
                                
                                counter+=1
            if counter == 0 and stop ==0:
                result += int(line2.rstrip().split(",")[len(line2.rstrip().split(","))//2])
        print("result"+str(result))
