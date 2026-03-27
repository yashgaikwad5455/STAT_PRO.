#To Find Number of Numbers From without Repeatation Using Perm()
from math import perm
digits=[1,2,3,4,5,6]
k=len(digits)
s=int(input("Enter The Number Of digits in Number:"))
print("No. of 4-digit Numbers Form:",perm(k,s))
