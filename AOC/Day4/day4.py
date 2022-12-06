def first(f):
    l=[]
    c=0
    for line in f:
        l=line.split("-")
        x=l[1].split(",")
        print(l[0], x[0], x[1], l[2])
        if(int(l[0])<=int(x[1]) and int(x[0])>=int(l[2])):
            c=c+1
        elif(int(x[1])<=int(l[0]) and int(l[2])>=int(x[0])):
            c=c+1
    print(c)

def second(f):
    l=[]
    c=0
    for line in f:
        l=line.split("-")
        x=l[1].split(",")
        print(l[0], x[0], x[1], l[2])
        if(int(l[0]) <= int(x[1]) <= int(x[0]) or  int(l[0]) <= int(l[2]) <= int(x[0])):
            c=c+1
        elif(int(x[1]) <= int(l[0]) <= int(l[2]) or  int(x[1]) <= int(x[0]) <= int(l[2])):
            c=c+1
    print(c)
# f = open("/Users/vishal.deshmukh/Desktop/AOC/Day4/input.txt", "r")
# first(f)
f = open("/Users/vishal.deshmukh/Desktop/AOC/Day4/input.txt", "r")
second(f)