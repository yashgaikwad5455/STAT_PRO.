#Q40 Simulation Bionomial Distribution n,P,N
import numpy as np
N=int(input("Enter Numbers of Simulatios:"))
p=float(input("Enter Probablity Of Success:"))
n=int(input("Enter Number Of Trials:"))
result=np.random.binomial(n,p,N)
print("X \t Freq \t Probability")
for x in range(n+1):
    feq=np.sum(result==x)
    pro=feq/N
    print(x,"\t",feq,"\t",pro)
print("Sample mean:",np.mean(result))
print("Sample variance:",np.var(result))
print("Th Sample mean:",(n*p))
print("Th Sample variance:",(n*p*(1-p)))
