from time import perf_counter as pfc
def solve(f, length1, length2, first, second):
    c=0
    firstSolved=False
    secondSolved=False
    for line in f:
        for i in line:
            c=c+1
            if(first and not firstSolved):
                if(c<length1): continue
                else:
                    s=line[c-length1:c]
                    if len(set(s)) == len(s):
                        print("Answer for First: "+str(c))
                        firstSolved=True
            if(second and not secondSolved):
                if(c<length2): continue
                else:
                    s=line[c-length2:c]
                    if len(set(s)) == len(s):
                        print("Answer for Second: "+str(c))
                        secondSolved=True
            if(firstSolved and secondSolved): break
start = pfc()
f = open("/Users/vishal.deshmukh/Desktop/AOC/Day6/input.txt", "r")
solve(f, 4, 14, True, True)
print(pfc()-start)
