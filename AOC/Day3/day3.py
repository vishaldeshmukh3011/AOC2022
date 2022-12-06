def first(f):
    t=0
    for line in f:
        l=len(line)
        a=line[0:(l//2)]
        b=line[l//2:l]
        c=list(set(a)&set(b))
        if(len(c)>1):
            print(line)
            print("*****")
            print(len(c))
        if c[0].islower():
            s=(ord(c[0])-96)
        else:
            s=(ord(c[0])-64+26)
        t=t+s
    print(t)

def second(f):
    t2=0
    l2=[]
    s2=0
    for line in f:
        l2.append(line.strip())
        if(len(l2)==3):
            c2=list(set(l2[0])&set(l2[1])&set(l2[2]))
            if c2[0].islower():
                s2=(ord(c2[0])-96)
            else:
                s2=(ord(c2[0])-64+26)
            t2=t2+s2
            l2=[]
    print(t2)
# f = open("/Users/vishal.deshmukh/Desktop/AOC/Day3/i.txt", "r")
# first(f)
f = open("/Users/vishal.deshmukh/Desktop/AOC/Day3/input.txt", "r")
second(f)


        
        

