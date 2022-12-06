f = open("/Users/vishal.deshmukh/Desktop/AOC/Day2/input.txt", "r")
scores1={
    'X':1,
    'Y':2,
    'Z':3
}
scores2={
    'X':0,
    'Y':3,
    'Z':6
}
scoreCheck={
    'A':{'X':3, 'Y':6, 'Z': 0},
    'B':{'X':0, 'Y':3, 'Z': 6},
    'C':{'X':6, 'Y':0, 'Z': 3}
}
secondQuestion={
    'A':{'X':3, 'Y':1, 'Z': 2},
    'B':{'X':1, 'Y':2, 'Z': 3},
    'C':{'X':2, 'Y':3, 'Z': 1}
}
t1=0
t2=0
def checkScore(a,b):
    if a =='A':
        if b=='X': return 3
        if b=='Y': return 6
        if b=='Z': return 0
    if a =='B':
        if b=='X': return 0
        if b=='Y': return 3
        if b=='Z': return 6
    if a =='C':
        if b=='X': return 6
        if b=='Y': return 0
        if b=='Z': return 3


for line in f:
    a=line[0]
    b=line[len(line)-2]
    #first question
    t1=t1+scoreCheck[a][b]
    t1=t1+scores1[b]

    #second Question
    t2=t2 + secondQuestion[a][b]
    t2=t2 + scores2[b]

print(str(t1) +" . " +str(t2))
