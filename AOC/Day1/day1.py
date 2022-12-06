f = open("/Users/vishal.deshmukh/Desktop/AOC/Day1/input.txt", "r")
s=0
l=[]
for line in f:
    if line=="\n":
        l.append(s)
        s=0
    else:
        s=s+int(line)
l.sort()
print("First: ", l[-1])
print("Second: ", l[-3:])