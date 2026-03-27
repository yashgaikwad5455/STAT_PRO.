#Q44 Solve 7P2 =60* 7Pr-3  Calculate value r=?
from math import perm
for r in range(3,8):
    if(perm(7,r)==60*perm(7,r-3)):
        print("Value of R is:",r)
        break
#Q45 Solve nC4:nC3 =11:1
from math import comb
for n in range(4,100):
    if (comb(n,4)/comb(n,3))==11:
        print("value Of N:",n)
        break
#Q46 Solve
for n in range(5,199):
    if perm(n,5)==240*comb(n,4):
        print("Value Of N is:",n)
        break
