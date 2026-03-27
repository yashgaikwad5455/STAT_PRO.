#Q33 Select Number Of Ways r Persons can Select n Different Chair
#Q34 Arrange Number Of Ways r Persons can Select n Different Chair
from itertools import permutations
from math import perm
n=int(input("Enter Total Number of Chairs:"))
r=int(input("Enter Total Number Of Persons:"))
result=perm(n,r)
print("Total Number Of Ways:",result)
person=['p1','p2','p3','p4','p5','p6']
result2=list(permutations(person,4))
for i in result2:
    print("".join(i))
    
print("Total Number Of Ways:",len(result2))
