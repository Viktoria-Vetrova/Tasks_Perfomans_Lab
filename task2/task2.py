import sys

shape=[]
dot=[]
with open(sys.argv[1],'r') as coordinates:
    for point in coordinates:
        shape.append([float(i) for i in point.split()])

with open(sys.argv[2], 'r') as points:
    for point in points:
        dot.append([float(i) for i in point.split()])


for x in range(len(dot)):
    array=[]
    for x1 in range(len(shape)):
        array.append((shape[x1][0]-dot[x][0])*(shape[(x1+1)%len(shape)][1]-shape[x1][1])\
        -(shape[(x1+1)%len(shape)][0]-shape[x1][0])*(shape[x1][1]-dot[x][1]))
    array = [int(i) for i in array]
    if array[0]<0 and array[1]<0 and array[2]<0 and array[3]<0:
        print('2')
    elif array.count(0)==2:
        print('0')
    elif array.count(0)==1 and array[0]<=0 and array[1]<=0 and array[2]<=0 and array[3]<=0:
        print('1')
    else:
        print('3')
    