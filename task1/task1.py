import sys

def percently_num(array):
  x = (90/100)*(len(array)-1)+1
  return array[int(x//1)-1]+x%1*(array[int(x//1)]-array[int(x//1)-1])

def median_num(array):
  if len(array)%2 == 1:
    return array[len(array)//2]
  if len(array)%2 == 0:
    return (array[(len(array)//2)-1]+array[len(array)//2])/2

def max_num(array):
  return array[len(array)-1]
  
def min_num(array):
  return array[0]
  
def avg_num(array):
  return sum(array)/len(array)

array=[]
with open(sys.argv[1], 'r') as numbers:
    for number in numbers:
        array.append(int(number))

array.sort()
   
print("%.2f" % percently_num(array))
print("%.2f" % median_num(array))
print("%.2f" % max_num(array))
print("%.2f" % min_num(array))
print("%.2f" % avg_num(array))