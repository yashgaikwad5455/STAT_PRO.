# Q35 & Q36
#Select 5 players from Grpoup of 10 Players
'''
1. Two players Out of 10 Always included..
2. Two Players Out Of 10 Always Excluded..
'''
from math import comb
n=int(input("Enter total Number of players in Group:"))
r=int(input("Enter Total Number of Players in Team/Selected:"))
i=int(input("Enter Number of Players include in Team/Selected:"))
e=int(input("Enter Number of Players exclude  in Team/Selected:"))
result=comb(n,r)
print("Total Number of Combinations:",result)
print("Total Number of Combinations Acc to coden 1:",comb(n-i,r-i))
print("Total Number of Combinations Acc to coden 1:",comb(n-e,r))
