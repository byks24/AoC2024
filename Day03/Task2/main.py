import re
result=0
dont=0
if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        for line in f: 
            regex = re.compile(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', re.I)
            regex2 = re.compile(r'\d+,\d+', re.I)
            for i in regex.findall(line):
                print(i)
                if i=="don\'t()": 
                    dont=1
                elif i=="do()": 
                    dont=0
                if dont==0 and i!="don\'t()" and i!="do()":
                    result+=int(regex2.findall(i)[0].split(',')[0])*int(regex2.findall(i)[0].split(',')[1])
        print(result)
