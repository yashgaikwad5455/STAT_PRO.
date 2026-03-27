#Select 3 Fruits From Given 6 Fruits use nCr
#Generate Cobnations Of Above
from math import comb
from itertools import combinations
n=int(input("Enter Total Number of fruits:"))
r=int(input("Enter Number Of Fruits be Selected:"))
result=comb(n,r)
print("All possible Selections:",result)
#Generate 3 Fruits From Given 6 Fruits use cobinations()
n=['f1','f2','f3','f4','f5','f6','f7']
r=3
result=list(combinations(n,r))
for i in result:
    print(i)
print("Total Number Of Different combinations:",len(result))
