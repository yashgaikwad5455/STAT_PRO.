#Q21-24
#Generate Possible Possword Using A-Z Alphabates with & Without
from itertools import permutations,combinations,product 
from math import perm,comb
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result2=list(product(alpha,repeat=4))
result1=list(permutations(alpha,r=4))
print("Generated All Possible Outcomes Without Repetations:",len(result1))
print("Generated All Possible Outcomes With Repetations:",len(result2))
# To Generate 4 shirts 3 pants and 2 pair Of shoes outfit Combinations
shirts=4
pants=3
shoes=2
result=shirts*pants*shoes
print("Total Number Combiantions:",result)
# Generate Total Number of outfits from Follwing Things(Use Product()) )
from itertools import product
shirts=['s1','s2','s3','s4']
pents=['p1','p2','p3']
shoes=['foramal','Proffestional']
result=list(product(shirts,pents,shoes))
for i in  result:
    print(i)
print("Total Number Of outfit Generated:",len(result))    

