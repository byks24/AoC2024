
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
            arr=line2.rstrip().split(",")
            all_good=1
            counter=0
            actions=0
            stop=0
            while all_good!=0 and stop==0:
                prev=[]
                counter=0
                for i in range(len(arr)):
                    prev.append(arr[i].rstrip())
                    for j in prev:
                        if arr[i].rstrip() in d1:
                            if j in d1[arr[i].rstrip()].split(","):

                                arr.insert(i+1,arr[i-1])
                                arr.pop(i-1)
                                counter+=1
                                actions+=1
                        else:
                                if len(arr)-1 != i:
                                    actions+=1
                                arr.append(arr[i])
                                arr.pop(i)
                                
                if counter == 0:
                    all_good=0
                    if actions>0:
                        result += int(arr[len(arr)//2])
        print("result"+str(result))
