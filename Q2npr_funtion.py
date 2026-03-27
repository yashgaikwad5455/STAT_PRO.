from math import factorial
def npr(n,r):
    return factorial(n)//factorial(n-r)
def ncr(n,r):
    return factorial(n)//factorial(r)*factorial(n-r)
print("8p3:",npr(8,3))
print("12c2:",ncr(12,2))
print("5p1:",npr(5,1))
print("5p5:",npr(5,5))
#using Perm()
from math import perm,comb
print("8p3:",perm(8,3))
print("8p3:",comb(8,3))
