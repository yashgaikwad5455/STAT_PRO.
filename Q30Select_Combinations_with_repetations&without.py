#Q30-31
#Select Combinations With Repetations And Without Repetations n+r-1Cr and nCr
#using Factorial Function & math module
from math import *
n=int(input("Enter Total Number of Fruits"))
r=int(input("Select Number of Fruits"))
with_result=comb(n,r)
with_manually=factorial(n)//(factorial(r)*factorial(n-r))
print("Total Number of Combinations without Repeatations:",with_result)
print("Total Number of Combinations without Repeatations Manully:",with_manually)
result=comb(n+r-1,r)
print("Total Number of Combinations with Repeatations:",result)
result2=factorial(n+r-1)//(factorial(r)*factorial(n+r-1-r))
print("Total Number of Combinations With Repations Mannualy:",result2)
