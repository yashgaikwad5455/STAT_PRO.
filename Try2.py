#Q39
import numpy as np
n=int(input("Enter Number Of trilas:"))
p=float(input("Enter The Probability Of Getting Success:"))
N=int(input("Enter number Of Simulations:"))
result=np.random.binomial(n,p,N)
print("X \t Freq \t Probability")
for x in range(n+1):
    freq=np.sum(result==x)
    pro=freq/N
    print(x,"\t",freq,"\t",pro)
