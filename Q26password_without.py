#Q26 & Q27
#Generate All Possible  Password Contain 2 Digits 0-9 and 2 Alphabates A-z
from itertools import permutations,product
digits="0123456789"
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr1=list(permutations(digits,2))
arr2=list(permutations(alpha,2))
count=0
for i in arr1:
    for j in arr2:
        print("".join(i+j))
        count+=1
print("Total Number of Without Repe arrangement:",count)
n=0
res1=list(product(digits,repeat=2))
res2=list(product(alpha,repeat=2))
for i in res1:
    for j in res2:
        print("".join(i+j))
        count+=1
print("Total Number of With Repe arrangement:",count)

