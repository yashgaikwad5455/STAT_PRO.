#Q37 Last Qes For Combinations
#Generate All Possible Outcomes is Team of 'r' players from 12 players use combinations
from itertools import combinations
group=[1,2,3,4,5,6,7,8,9,10,11,12]
r=int(input("\n Enter total Players In Team:"))
result=list(combinations(group,r))
n=1
for i in result:
    print(f"Team{n} Players:{i}",end="\n")
    n+=1
print("Total Numbers Of Different Teams:",n-1)





