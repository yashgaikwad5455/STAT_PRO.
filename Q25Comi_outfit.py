#Generate combinations with Destriction 
from itertools import product
shirt=['Red','Blue']
paint=['Blue','White']
shoe=['Formal','sport']
outfit=list(product(shirt,paint,shoe))
count=0
for x,y,z in outfit:
    if not(y=='White' and z=='sport'):
        print(x,y,z)
        count+=1
print("Total Possible Combiantions:",count)

