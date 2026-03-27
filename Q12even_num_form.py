#To find no. of 4-Digits even Number Can  From by digits
from math import perm,factorial
digits=[1,2,3,4,5,6,7,8,]
even=[2,4,6,8]
count=0
for i in even:
    n=0
    for j in digits:
        if i!=j:
            n=n+1
    count=count+factorial(n)//factorial(n-3)
print("Total 4 digits Even Numbers can Form:",count)

print()
print("Using Perm Function")
n=len(digits)
k=0
for i in digits:
    if i%2==0:
        k=k+1
count=k*perm(n-1,3)
print("Total 4 digits Even Numbers can Form:",count)
        

            
