# Program to find power set of a set
import math;
def printPowerSet(set, setSize):
    powersetSize = (int)(math.pow(2,setSize));
    outer = 0;
    inner = 0;
    for outer in range(0,powersetSize):
      for inner in range(0,setSize):
         if((outer&(1<<inner))>0):
            print(set[inner],end = "")
      print("")    
size = int(input("Enter array size:"))
set = []
for i in range(0,size):
   n = int(input("Enter elements:"))
   set.append(n)
printPowerSet(set, len(set))