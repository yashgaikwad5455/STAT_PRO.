#Find The number of numbers which greater tha 5000 and divisble by 5
from math import factorial
digits=[1,2,3,4,5,6,7,8]
n=len(digits)
print("Number of 4-digit Numbers Formed:",factorial(n)//factorial(n-4))
# Greater than 5000
k=0
for i in digits:
    if i>=5:
        k=k+1
n1=n-1
print("Total Number of numbers Greater Than 5000 :",k*factorial(n1)//factorial(n1-3))
l=0
for i in digits:
    if i>5:
        l=l+1
n2=n-2
print("Total Number of numbers Greater Than 5000 And Divisible byb 5 :",k*factorial(n2)//factorial(2))

