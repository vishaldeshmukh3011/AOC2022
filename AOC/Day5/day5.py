import copy
from time import perf_counter as pfc
def solve(f):
    l=[]
    s=[]
    second_l = []
    firstRow=True
    for line in f:
        c=0
        if('[' in line):
            i=1
            while i<len(line):
                if firstRow:
                    s=[]
                    if(line[i]!=' '):
                        s.insert(0,line[i])
                    l.append(s)    
                else:
                    s=l[c]
                    if(line[i]!=' '):
                        s.insert(0,line[i])
                i=i+4
                c=c+1
        else:
            if line[0] == ' ':
                continue
            elif line[0] == 'm':
                if(second_l==[]):
                    second_l=copy.deepcopy(l)
                first_problem(l, line)
                second_problem(second_l, line)
        firstRow=False
        
    print("First Problem Solution")
    for j in l:
        print(j[-1])
    print("Second Problem Solution")
    for j in second_l:
        print(j[-1])

def first_problem(l,line):
    a=line.strip().split(" ")
    x=int(a[1])
    y=int(a[3])
    z=int(a[5])
    for k in range(0,x):
        temp=l[y-1].pop(-1)
        l[z-1].append(temp)
    

def second_problem(p,line):
    a=line.strip().split(" ")
    x=int(a[1])
    y=int(a[3])
    z=int(a[5])
    s=len(p[y-1])-x
    for k in range(0,x):
        temp=p[y-1].pop(s)
        p[z-1].append(temp)

start = pfc()
f = open("/Users/vishal.deshmukh/Desktop/AOC/Day5/i.txt", "r")
l=solve(f)
print(pfc()-start)
