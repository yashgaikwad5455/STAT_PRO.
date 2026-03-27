#Q32 
#Select Fruits Out Of Fruits With Replacement
from itertools import combinations_with_replacement
fruits=['Apple','Banana','Graps','Gauua','Orange','Mango']
r=int(input("Enter Number Of Fruits to be select:"))
result=list(combinations_with_replacement(fruits,r))
for i in result:
    print(" ".join(i),end="\n ")
print("Total Number of Combinations With Replacement:",len(result))
