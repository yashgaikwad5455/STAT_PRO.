#Q39 Simulate 1000 die rolling At time  Calculate Probability Of Getting 1,2,3,4,5,6
import numpy as np
N=int(input("Enter Number Of Simulations Of Die:"))
sample=[1,2,3,4,5,6]
result=np.random.choice(sample,size=N)
print("Face \t Frequency \t Probability")
for i in range(1,7):
    feq=np.sum(result==i)
    pro=feq/N
    print(i,"\t",feq,"\t \t",pro)

