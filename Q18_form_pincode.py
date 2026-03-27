#Form 4-digits pincode from given number of digits with repetation and without rerpetation
# With Repetation= n**r & Without Repetation nPr
from itertools import permutations,product
from math import factorial
digits=[1,2,3,4,5,6,7,8,9]
r=int(input("\n Enter Total Number oF Digits in Pin code:"))
n=len(digits)
with_re=n**r
print("Total Numbers of Pin codes With Repetations:",with_re)
witho_re=factorial(n)//factorial(n-r)
print("Total Numbers of Pin codes Without Repetations:",witho_re)
#Simple Program To generate 4 Digits numbers using 0-9 Digits
d=[1,2,3,4,5,6,7,8,9]
result=list(product(d,repeat=4))
result2=list(permutations(d,r=4))
print(len(result2))
print(len(result))
