with open("text.txt") as fin:
    line = fin.read().strip()

def make_fs(diskmap):
    blocks=[]

    is_file = True
    id = 0
    for x in diskmap:
        x = int(x)
        if is_file:
            blocks += [id] * x
            id +=1
            is_file= False
        else:
            blocks += [None] * x
            is_file = True
    return blocks

fs= make_fs(line)

def prettyprint(arr):
    for char in arr:
        print(char if char != None else ".", end="")
    print()

def move(arr):
    first_free =0
    while arr[first_free]!= None:
        first_free+=1
    i = len(arr) -1
    while arr[i] == None:
        i-=1
    while i > first_free:
        arr[first_free] = arr[i]
        arr[i] = None
        while arr[i]==None:
            i-=1
        while arr[first_free] != None:
            first_free+=1
    return arr

def checksum(arr):
    ans =0
    for i,x in enumerate(arr):
        if x != None:
            ans += i * x
    return(ans)
moved = move(fs)
print(checksum(moved))